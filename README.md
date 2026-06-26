# ValorAI

A modern framework and use case library for measuring the true financial value of AI. Focused on rigorous assessment methodologies, ROI modelling, value realisation, and decision frameworks that turn AI potential into measurable business outcomes.

**Site:** https://felipelago17.github.io/valorai/

---

## What This Repository Contains

ValorAI is structured as an evidence-based knowledge base anchored to Douglas Hubbard's measurement discipline. The central argument: most AI valuations omit 40–60% of true costs, and a defensible valuation must therefore be a *measurement discipline*, not a ritual.

### Framework Structure

```
docs/
  index.md                          # Framework overview + Hubbard core test
  methodology/
    measurement-discipline.md       # Hubbard lens + scientific method applied to PM
    valuation-models.md             # TCO, ROI/NPV/IRR, real options, value-of-information
  indirect-costs/
    index.md                        # Taxonomy overview + 40–60% hidden-cost thesis
    technical-debt.md               # ML maintenance debt (Sculley et al.)
    integration-implementation.md   # Hidden integration costs; 2–3× expansion
    verification-oversight.md       # The verification tax on efficiency gains
    cognitive-human-capital.md      # Deskilling, automation bias, cognitive offloading
    environmental-externalities.md  # Carbon, water, land, e-waste footprints
    labour-supply-chain.md          # Ghost work, ESG exposure (Gray & Suri)
    governance-shadow-ai.md         # Shadow AI economy (MIT NANDA)
  evidence/
    bibliography.md                 # Annotated reference list
    base-rates.md                   # Key quantitative findings, citable table
  use-cases/
    index.md                        # Use-case library (forthcoming)
```

### Key Evidence

| Finding | Figure | Source |
|---|---|---|
| Hidden costs as share of total AI project cost | 40–60% | Gartner / Meta-Intelligence (2025) |
| Enterprises that can quantify AI business value | ~13% | MIT Sloan (via Meta-Intelligence) |
| GenAI pilots with no measurable P&L impact | ~95% | MIT NANDA (2025) |
| Total cost expansion beyond initial budget | 2–3× | Anyreach (2026) |
| Workers using personal (shadow) AI tools at work | ~90% | MIT NANDA (2025) |

---

## Running the Site Locally

```bash
pip install mkdocs-material
mkdocs serve
```

The site will be available at `http://localhost:8000`.

To build a static site for deployment:

```bash
mkdocs build --strict
```

---

## Deployment

The site is deployed automatically to GitHub Pages via the workflow in `.github/workflows/deploy.yml` on every push to `main`.

---

## Methodological Anchor

The framework's methodological spine is Douglas W. Hubbard's *How to Measure Anything in Project Management* (Wiley). The core test applied to every valuation method in the framework:

> *Does the method measurably improve judgement under uncertainty?*

A method that produces confident-looking numbers without improving actual decisions is an **analysis placebo** — process that raises certainty without raising accuracy. ValorAI's indirect-cost taxonomy and full-lifecycle TCO model are designed to pass this test by making the full cost of AI ownership visible and anchoring projections to empirically-derived base rates.
