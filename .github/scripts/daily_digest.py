#!/usr/bin/env python3
"""Daily news digest builder.

Pulls items from RSS feeds, HTML listing pages and the Federal Register API,
keeps only those matching the repository's KEYWORDS and published within the
look-back window, and prepends a dated block to the digest page between the
DIGEST_START / DIGEST_END markers. Safe to run daily; sources that fail are
logged and skipped, never fatal.
"""
import datetime as dt
import json
import re
import socket
import sys
from pathlib import Path

socket.setdefaulttimeout(30)

import feedparser
import requests
from bs4 import BeautifulSoup

# ---- Repository configuration ----
BOT_NAME = 'valorai-digest-bot/1.0'
REPO_URL = 'https://github.com/felipelago17/valorai'
LOOKBACK_HOURS = 36
MAX_PER_CATEGORY = 12
MAX_LINES = 4000
DIGEST_PATHS = ['docs/news/digest.md']
DATA_JSON = 'data/digest-latest.json'
CATEGORY_ORDER = ['Research & Working Papers',
 'Management & Strategy',
 'Industry & Market',
 'Energy & Infrastructure Cost']
KEYWORDS = ['return on investment',
 'roi',
 'total cost of ownership',
 'tco',
 'business value',
 'productivity',
 'ai adoption',
 'ai investment',
 'ai spending',
 'ai spend',
 'capex',
 'opex',
 'payback',
 'net present value',
 'npv',
 'unit economics',
 'inference cost',
 'cost per token',
 'token price',
 'gpu',
 'compute cost',
 'data center',
 'data centre',
 'datacenter',
 'energy cost',
 'electricity',
 'power demand',
 'pilot',
 'proof of concept',
 'scale',
 'failure rate',
 'abandon',
 'shadow ai',
 'technical debt',
 'integration cost',
 'implementation cost',
 'change management',
 'upskilling',
 'reskilling',
 'workforce',
 'labor market',
 'labour market',
 'job',
 'wage',
 'oversight cost',
 'human in the loop',
 'verification',
 'hallucination',
 'error rate',
 'rework',
 'agentic',
 'ai agent',
 'copilot',
 'generative ai',
 'genai',
 'llm',
 'large language model',
 'enterprise ai',
 'vendor',
 'pricing',
 'subscription',
 'seat',
 'license',
 'licence',
 'measurement',
 'kpi',
 'metric',
 'value realization',
 'value realisation',
 'business case',
 'mckinsey',
 'gartner',
 'survey',
 'cfo',
 'cio',
 'earnings',
 'capital expenditure']
RSS_SOURCES = [('NBER Working Papers', 'https://www.nber.org/rss/new.xml', 'Research & Working Papers'),
 ('arXiv econ.GN', 'https://rss.arxiv.org/rss/econ.GN', 'Research & Working Papers'),
 ('arXiv cs.CY', 'https://rss.arxiv.org/rss/cs.CY', 'Research & Working Papers'),
 ('MIT Sloan Management Review', 'https://sloanreview.mit.edu/feed/', 'Management & Strategy'),
 ('Harvard Business Review', 'https://feeds.hbr.org/harvardbusiness', 'Management & Strategy'),
 ('McKinsey Insights', 'https://www.mckinsey.com/insights/rss', 'Management & Strategy'),
 ('Brookings', 'https://www.brookings.edu/feed/', 'Research & Working Papers'),
 ('MIT Technology Review', 'https://www.technologyreview.com/feed/', 'Industry & Market'),
 ('Stanford HAI', 'https://hai.stanford.edu/news/rss.xml', 'Research & Working Papers'),
 ('Data Center Dynamics',
  'https://www.datacenterdynamics.com/en/rss/',
  'Energy & Infrastructure Cost'),
 ('Uptime Institute Journal',
  'https://journal.uptimeinstitute.com/feed/',
  'Energy & Infrastructure Cost'),
 ('CSET', 'https://cset.georgetown.edu/feed/', 'Research & Working Papers')]
HTML_SOURCES = [('IEA News',
  'https://www.iea.org/news',
  "a[href*='/news/']",
  'https://www.iea.org',
  'Energy & Infrastructure Cost',
  True),
 ('Gartner Newsroom',
  'https://www.gartner.com/en/newsroom',
  "a[href*='/newsroom/press-releases/']",
  'https://www.gartner.com',
  'Industry & Market',
  True)]
FEDERAL_REGISTER_TERMS = []

# ---------------------------------------------------------------------------
TODAY = dt.date.today()
CUTOFF = dt.datetime.now(dt.timezone.utc).replace(tzinfo=None) - dt.timedelta(hours=LOOKBACK_HOURS)
HEADERS = {"User-Agent": f"Mozilla/5.0 (compatible; {BOT_NAME}; +{REPO_URL})"}
KEYWORDS_LC = [k.lower() for k in KEYWORDS]

items = []          # (title, url, source, category)
seen = set()


def log(msg):
    print(msg, file=sys.stderr)


def relevant(text):
    t = text.lower()
    return any(k in t for k in KEYWORDS_LC)


def add(title, url, source, category):
    title = re.sub(r"\s+", " ", title or "").strip()
    url = (url or "").strip()
    key = url.split("?")[0].rstrip("/")
    if not title or not url or key in seen or len(title) < 12:
        return
    seen.add(key)
    items.append((title, url, source, category))


def get(url, timeout=25):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        r.raise_for_status()
        return r.text
    except Exception as e:  # noqa: BLE001
        log(f"  WARN {url} -> {e}")
        return ""


# --- RSS ------------------------------------------------------------------
for label, feed_url, category in RSS_SOURCES:
    try:
        raw = get(feed_url)
        if not raw:
            continue
        feed = feedparser.parse(raw)
        n = 0
        for e in feed.entries[:60]:
            title = e.get("title", "")
            url = e.get("link", "")
            pub = e.get("published_parsed") or e.get("updated_parsed")
            if pub:
                try:
                    if dt.datetime(*pub[:6]) < CUTOFF:
                        continue
                except Exception:  # noqa: BLE001
                    pass
            summary = e.get("summary", "") or ""
            if e.get("content"):
                summary += " " + (e["content"][0].get("value") or "")
            if title and url and relevant(title + " " + summary):
                add(title, url, label, category)
                n += 1
        log(f"  RSS {label}: {len(feed.entries)} entries, {n} kept")
    except Exception as e:  # noqa: BLE001
        log(f"  RSS error [{label}]: {e}")

# --- HTML listing pages ---------------------------------------------------
for label, page_url, selector, base, category, require_kw in HTML_SOURCES:
    html = get(page_url)
    if not html:
        continue
    soup = BeautifulSoup(html, "lxml")
    n = 0
    for a in soup.select(selector)[:15]:
        title = a.get_text(" ", strip=True)
        href = a.get("href", "")
        if not title or not href:
            continue
        if require_kw and not relevant(title):
            continue
        full = href if href.startswith("http") else base.rstrip("/") + "/" + href.lstrip("/")
        add(title, full, label, category)
        n += 1
    log(f"  HTML {label}: {n} kept")

# --- Federal Register -----------------------------------------------------
if FEDERAL_REGISTER_TERMS:
    for term in FEDERAL_REGISTER_TERMS:
        url = (
            "https://www.federalregister.gov/api/v1/documents.json"
            "?fields[]=title&fields[]=html_url&fields[]=publication_date&fields[]=abstract"
            f"&order=newest&per_page=20&conditions[term]={requests.utils.quote(term)}"
            f"&conditions[publication_date][gte]={(TODAY - dt.timedelta(days=2)).isoformat()}"
        )
        try:
            data = requests.get(url, headers=HEADERS, timeout=25).json()
            for doc in data.get("results", []):
                t, u, pub = doc.get("title", ""), doc.get("html_url", ""), doc.get("publication_date", "")
                if t and u and relevant(t + " " + (doc.get("abstract") or "")):
                    add(f"{t} ({pub})", u, "Federal Register", "Official & Regulatory")
        except Exception as e:  # noqa: BLE001
            log(f"  Federal Register error [{term}]: {e}")

# --- Build block ----------------------------------------------------------
by_cat = {}
for title, url, source, cat in items:
    by_cat.setdefault(cat, []).append((title, url, source))

lines = [f"## {TODAY.isoformat()}", ""]
if not items:
    lines += ["*No new relevant items retrieved today.*", ""]
else:
    for cat in CATEGORY_ORDER + [c for c in by_cat if c not in CATEGORY_ORDER]:
        entries = by_cat.get(cat)
        if not entries:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        for title, url, source in entries[:MAX_PER_CATEGORY]:
            safe_title = title.replace("[", "(").replace("]", ")")
            lines.append(f"- **[{source}]** [{safe_title}]({url})")
        lines.append("")
new_block = "\n".join(lines).rstrip() + "\n"

# --- Inject ---------------------------------------------------------------
START, END = "<!-- DIGEST_START -->", "<!-- DIGEST_END -->"
for path in DIGEST_PATHS:
    p = Path(path)
    if not p.exists():
        log(f"  WARN digest file missing: {path}")
        continue
    content = p.read_text(encoding="utf-8")
    m = re.search(re.escape(START) + r"(.*?)" + re.escape(END), content, flags=re.S)
    existing = m.group(1).strip() if m else ""
    if existing.startswith("*First run pending"):
        existing = ""
    if existing.startswith(f"## {TODAY.isoformat()}"):
        # already ran today: replace today's block instead of duplicating it
        parts = re.split(r"\n(?=## \d{4}-\d{2}-\d{2})", existing, maxsplit=1)
        existing = parts[1].strip() if len(parts) > 1 else ""
    combined = new_block.splitlines() + (["", "---", ""] + existing.splitlines() if existing else [])
    combined = combined[:MAX_LINES]
    body = "\n".join(combined).rstrip()
    new_content = (
        content[: m.start()] + f"{START}\n{body}\n{END}" + content[m.end():]
        if m
        else content.rstrip() + f"\n\n{START}\n{body}\n{END}\n"
    )
    p.write_text(new_content, encoding="utf-8")
    log(f"  Written: {path}")

# machine-readable copy for downstream tooling
if DATA_JSON:
    Path(DATA_JSON).parent.mkdir(parents=True, exist_ok=True)
    Path(DATA_JSON).write_text(
        json.dumps(
            {"date": TODAY.isoformat(), "items": [
                {"title": t, "url": u, "source": s, "category": c} for t, u, s, c in items
            ]},
            indent=2, ensure_ascii=False,
        ),
        encoding="utf-8",
    )

print(f"Done. {len(items)} items collected for {TODAY.isoformat()}.")
