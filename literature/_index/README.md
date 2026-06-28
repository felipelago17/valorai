# Literature Index

This directory is the central index for the `literature/` knowledge base.

- **`schema.md`** — canonical YAML front-matter schema and controlled vocabulary
- **`bibliography.md`** — flat alphabetical reference list of all seeded sources
- **This file** — value-cost ledger model, source table, and contribution guide

---

## The Value-Cost Ledger Model

Every source in this library is tagged against two dimension lists that together define the two sides of the AI valuation ledger.

### Value dimensions (benefit side)

| Dimension | What it captures |
|---|---|
| `productivity` | Output per unit of time or effort — speed, throughput, capacity |
| `quality` | Accuracy, consistency, error rate, rework rate |
| `revenue` | Incremental revenue from AI-enabled products or services |
| `cost-to-serve` | Reduction in operational or delivery cost per unit |
| `time-returned` | Calendar time saved that can be reallocated to higher-value work |
| `decision-quality` | Measurable improvement in the quality of decisions made |

### Cost dimensions (indirect-cost side)

| Dimension | What it captures |
|---|---|
| `financial-tco` | Licensing, compute, integration, maintenance, and hidden ramp costs |
| `time` | Human time absorbed by AI management, prompt engineering, verification |
| `privacy-data-security` | Data-handling risk, breach exposure, compliance overhead |
| `environmental` | Energy consumption, carbon footprint, freshwater use of AI infrastructure |
| `labor-employment` | Workforce displacement, wage effects, transition and retraining cost |
| `cognitive-skills` | Deskilling, cognitive offloading, long-run human-capital erosion |
| `trust-accountability` | Automation bias, hallucination risk, liability, auditability gaps |
| `social-wellbeing` | Distributional effects, dependency, meaning-of-work, social externalities |

A source may be tagged to multiple dimensions. The `stance` field (`value-positive`, `cost-cautionary`, `mixed`, `reality-check`) provides the net editorial signal for a given source.

---

## Seeded Sources

| Source | Year | Type | Primary sector | Stance | Value dims | Cost dims |
|---|---|---|---|---|---|---|
| McKinsey Global Institute — *The Economic Potential of Generative AI* | 2023 | industry-report | cross-sector | value-positive | productivity, quality, revenue, cost-to-serve | — |
| Maslej et al. (Stanford HAI) — *AI Index Report 2025* | 2025 | industry-report | cross-sector | mixed | productivity, quality | financial-tco, environmental |
| Brynjolfsson, Li & Raymond — *Generative AI at Work* | 2023 | working-paper | 11-technology-software-telecom | value-positive | productivity, quality, time-returned | — |
| Noy & Zhang — *Experimental evidence on the productivity effects of GenAI* | 2023 | journal-article | 04-legal-compliance-professional-services | value-positive | productivity, quality, time-returned | — |
| Dell'Acqua et al. — *Navigating the Jagged Technological Frontier* | 2023 | working-paper | 04-legal-compliance-professional-services | mixed | productivity, quality | cognitive-skills, trust-accountability |
| Acemoglu — *The Simple Macroeconomics of AI* | 2025 | journal-article | cross-sector | reality-check | — | financial-tco, labor-employment |
| Challapally et al. (MIT NANDA) — *The GenAI Divide* | 2025 | industry-report | cross-sector | reality-check | — | financial-tco |
| Stern — *I Am Not a Robot* | 2026 | journalism | 15-consumer-personal-household | cost-cautionary | — | cognitive-skills, social-wellbeing |
| Luccioni, Jernite & Strubell — *Power Hungry Processing* | 2024 | conference-paper | cross-sector | cost-cautionary | — | environmental |
| Li et al. — *Making AI Less "Thirsty"* | 2023 | working-paper | cross-sector | cost-cautionary | — | environmental |
| IEA — *Energy and AI* | 2025 | gov-report | 03-energy-utilities | cost-cautionary | — | environmental |
| Acemoglu & Restrepo — *Tasks, Automation, and the Rise in US Wage Inequality* | 2022 | journal-article | 14-human-capital-hr-future-of-work | cost-cautionary | — | labor-employment |
| Lee et al. — *The Impact of Generative AI on Critical Thinking* | 2025 | conference-paper | cross-sector | cost-cautionary | — | cognitive-skills, trust-accountability |
| Kosmyna et al. — *Your Brain on ChatGPT* | 2025 | working-paper | 09-education-edtech | cost-cautionary | — | cognitive-skills |
| Becker et al. (METR) — *Measuring the Impact of Early-2025 AI on Experienced OS Dev Productivity* | 2025 | working-paper | cross-sector | reality-check | productivity, time-returned | time, trust-accountability, cognitive-skills |
| Glean Work AI Institute — *The Work AI Index 2026* | 2026 | industry-report | cross-sector | reality-check | productivity, time-returned | time, trust-accountability, cognitive-skills, labor-employment |

---

## How to Add a Source

1. **Read `schema.md`** to understand the required YAML front-matter fields and controlled vocabulary.

2. **Determine filing location:**
   - If the source primarily concerns one sector (e.g., healthcare, energy), file it under `sectors/NN-slug/`.
   - If it is cross-sector and the dominant signal is a cost dimension, file it under `_cross-cutting/<dominant-cost-lens>/`.
   - If it is cross-sector and value-positive (or reality-check with no dominant cost lens), file it under `_cross-cutting/financial-tco/`.

3. **Create the note file** following the naming convention `author-year-slug.md` (lowercase, hyphens, no spaces). Use only ASCII characters.

4. **Populate the front matter** with all required fields. Tag all applicable `value_dimensions` and `cost_dimensions` (lists, even if only one item). Use `[VERIFY]` inline where a specific detail (DOI, edition, venue) has not been independently confirmed.

5. **Write the four body sections:** Summary · What it lets valorai measure · Caveats / limits · Citation.

6. **Add the source to this table** (README.md) and to `bibliography.md` in alphabetical order.

7. **Commit** with the prefix `lit:` (e.g., `lit: add Surname (YYYY) — short descriptor`).
