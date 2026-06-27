# Source Library

The ValorAI source library catalogues the research, reports, and books that underpin the framework's value and cost estimates. Every source is tagged against a two-sided ledger — the benefit dimensions on the left, the indirect-cost dimensions on the right — so that a reader can trace any figure in the framework back to its evidentiary base.

Full notes for each source, including detailed YAML metadata, caveats, and complete citations, live in the [`literature/`](https://github.com/felipelago17/valorai/tree/main/literature) directory of the repository.

---

## The Value-Cost Ledger

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

A source may be tagged to multiple dimensions on either side. The **stance** field (`value-positive`, `cost-cautionary`, `mixed`, `reality-check`) provides the net editorial signal.

---

## Seeded Sources

| Source | Year | Type | Sector | Stance | Value dims | Cost dims |
|---|---|---|---|---|---|---|
| McKinsey Global Institute — *The Economic Potential of Generative AI* | 2023 | industry-report | cross-sector | value-positive | productivity, quality, revenue, cost-to-serve | — |
| Maslej et al. (Stanford HAI) — *AI Index Report 2025* | 2025 | industry-report | cross-sector | mixed | productivity, quality | financial-tco, environmental |
| Brynjolfsson, Li & Raymond — *Generative AI at Work* | 2023 | working-paper | technology / software | value-positive | productivity, quality, time-returned | — |
| Noy & Zhang — *Experimental Evidence on the Productivity Effects of GenAI* | 2023 | journal-article | legal / professional services | value-positive | productivity, quality, time-returned | — |
| Dell'Acqua et al. — *Navigating the Jagged Technological Frontier* | 2023 | working-paper | legal / professional services | mixed | productivity, quality | cognitive-skills, trust-accountability |
| Acemoglu — *The Simple Macroeconomics of AI* | 2025 | journal-article | cross-sector | reality-check | — | financial-tco, labor-employment |
| Challapally et al. (MIT NANDA) — *The GenAI Divide* | 2025 | industry-report | cross-sector | reality-check | — | financial-tco |
| Stern — *I Am Not a Robot* | 2026 | book | consumer / personal | cost-cautionary | — | cognitive-skills, social-wellbeing |
| Luccioni, Jernite & Strubell — *Power Hungry Processing* | 2024 | conference-paper | cross-sector | cost-cautionary | — | environmental |
| Li et al. — *Making AI Less "Thirsty"* | 2023 | working-paper | cross-sector | cost-cautionary | — | environmental |
| IEA — *Energy and AI* | 2025 | gov-report | energy / utilities | cost-cautionary | — | environmental |
| Acemoglu & Restrepo — *Tasks, Automation, and the Rise in US Wage Inequality* | 2022 | journal-article | human capital / HR | cost-cautionary | — | labor-employment |
| Lee et al. — *The Impact of Generative AI on Critical Thinking* | 2025 | conference-paper | cross-sector | cost-cautionary | — | cognitive-skills, trust-accountability |
| Kosmyna et al. — *Your Brain on ChatGPT* | 2025 | working-paper | education / edtech | cost-cautionary | — | cognitive-skills |

---

## Adding a Source

1. Read [`literature/_index/schema.md`](https://github.com/felipelago17/valorai/blob/main/literature/_index/schema.md) for the YAML front-matter specification and controlled vocabulary.
2. Determine filing location: sector-specific notes go in `literature/sectors/NN-slug/`; cross-sector notes go in `literature/_cross-cutting/<dominant-cost-lens>/`.
3. Create a note file named `author-year-slug.md` and populate all required fields.
4. Add the source to the table above and to [`literature/_index/bibliography.md`](https://github.com/felipelago17/valorai/blob/main/literature/_index/bibliography.md).
5. Commit with the prefix `lit:`.
