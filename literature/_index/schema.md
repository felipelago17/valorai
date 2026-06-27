# Metadata Schema & Tagging Conventions

Every literature note in this repository is a Markdown file with YAML front matter followed by a structured body. The schema is reproduced here verbatim for reference.

---

## YAML Front Matter

```yaml
---
title:
authors:
year:
type:            # book | journal-article | working-paper | industry-report | gov-report | dataset
publisher:
identifier:      # ISBN / DOI / NBER no. / URL
primary_sector:  # one sectors/NN slug, or "cross-sector"
sectors:         # all relevant sector slugs (list)
value_dimensions:   # subset of the value list (see below)
cost_dimensions:    # subset of the cost list (see below)
stance:          # value-positive | cost-cautionary | mixed | reality-check
also_cited_in:   # optional — path(s) to other valorai files that cite this work
key_metrics:     # 1-3 quantified claims, if any
relevance_to_valorai:  # one line: what this lets us measure
---
```

---

## Controlled Vocabulary

### Value Dimensions
- `productivity` — throughput and output-per-unit-input gains
- `quality` — accuracy, error-rate, or rated-quality improvements
- `revenue` — new revenue streams or revenue-expansion potential
- `cost-to-serve` — reduction in unit cost of delivering a service or product
- `time-returned` — time saved per task or decision cycle
- `decision-quality` — improvement in decision accuracy or outcomes

### Cost Dimensions
- `financial-tco` — full lifecycle financial cost (subscriptions, infrastructure, integration, maintenance)
- `time` — error-correction overhead, verification burden, friction costs
- `privacy-data-security` — data-handling risk, breach exposure, regulatory compliance
- `environmental` — energy, water, carbon, land, e-waste
- `labor-employment` — displacement, wage effects, supply-chain labour conditions
- `cognitive-skills` — deskilling, automation bias, critical-thinking erosion
- `trust-accountability` — liability, explainability, due-process, audit obligations
- `social-wellbeing` — dependency, companionship effects, mental health, equity

### Stance
- `value-positive` — primary contribution is documenting or quantifying value/benefit
- `cost-cautionary` — primary contribution is documenting or quantifying cost/risk
- `mixed` — substantive evidence on both value and cost sides
- `reality-check` — corrects inflated estimates or highlights the gap between expectation and evidence

---

## Body Structure (≤ 200 words)

```markdown
## Summary

[Paraphrase of the work's argument, findings, and scope.]

## What it lets valorai measure

[One or two sentences on the specific measurement capability this source enables.]

## Caveats / limits

[Sample size, methodology, scope, sponsorship, or other reliability limits.]

## Citation

Author(s) (year). *Title.* Publisher/Venue. Identifier.
```

---

## Filing Rules

- Place the note in its `primary_sector/` folder.
- If `primary_sector: cross-sector`, file under `_cross-cutting/<dominant-cost-lens>/`.
  For value-positive or reality-check cross-sector sources with no dominant cost lens, file under `_cross-cutting/financial-tco/`.
- Tag all relevant sectors in the `sectors:` list so the index can regroup sources by sector.

## File Naming

`authorlastname-year-shortslug.md`

Examples:
- `stern-2026-i-am-not-a-robot.md`
- `brynjolfsson-2023-genai-at-work.md`
- `iea-2024-electricity.md`

## Adding a Source

1. Create a new `.md` file following the naming convention above.
2. Copy the YAML front matter template and populate all fields.
3. Write the four-section body (≤ 200 words total).
4. File in the correct folder per the filing rules.
5. Add an entry to `_index/bibliography.md` (alphabetical by first author surname).
6. Update the source table in `_index/README.md`.
