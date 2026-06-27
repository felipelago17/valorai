# Base Rates

The table below consolidates key quantitative findings that inform the ValorAI indirect-cost framework. Each entry identifies the finding, the figure, and the source. Where a figure is an estimate or a range, this is indicated. Where independent verification of the specific citation is advised, entries are marked `[VERIFY]`.

These figures are not assumptions — they are empirical reference points. A valuation that produces estimates substantially more optimistic than these base rates should be treated with scepticism and subjected to additional scrutiny.

---

## Quantitative Findings

| Finding | Figure | Source |
|---|---|---|
| Firms underestimate AI TCO when focusing on subscription costs only | 40–60% of true costs hidden | Gartner (via Anyreach 2026) |
| Hidden costs as share of total AI project cost | 40–60% | Meta-Intelligence (2025), citing independent research |
| Enterprises able to quantify AI business value | ~13% | MIT Sloan Management Review (via Meta-Intelligence 2025) |
| GenAI pilots with no measurable P&L impact | ~95% | MIT NANDA, *The GenAI Divide* (2025) |
| Total project cost expansion beyond initial budget | 2–3× | Anyreach (2026) |
| Workers using personal AI tools at work | ~90% | MIT NANDA, *The GenAI Divide* (2025) |
| Workers using officially provisioned AI tools | ~40% | MIT NANDA, *The GenAI Divide* (2025) |
| Water consumption per kWh of data-centre energy (cooling) | ~2 L/kWh | MIT News (2025) `[VERIFY]` |
| AI carbon footprint, 2025 (estimated range) | 32.6–79.7 Mt CO₂e | ScienceDirect (2025) `[VERIFY specific article]` |
| AI water footprint, 2025 (estimated range) | 312.5–764.6 bn L | ScienceDirect (2025) `[VERIFY specific article]` |
| Internal AI builds that stall, relative to externally-integrated systems | ~3× higher rate | Anyreach (2026) `[VERIFY]` |
| McKinsey GenAI annual economic value estimate | $2.6–4.4 tn/year | McKinsey Global Institute `[VERIFY edition]` |
| Gartner agentic-AI enterprise abandonment forecast | >40% of projects by 2027 | Gartner (2024) `[VERIFY]` |
| AI initiatives failing to deliver measurable value (energy sector) | Up to 95% | AI in Energy Summit 2026 Insights Report [A] (self-reported, 130+ leaders) |
| Energy organisations highly prepared for AI (workflows embedded, staff AI-fluent) | 17% | AI in Energy Summit 2026 Insights Report [A] (self-reported) |
| Minimum accuracy threshold for production AI trust (energy sector) | ~85% | AI in Energy Summit 2026 Insights Report [A] (self-reported) |
| Energy & utilities AI adoption rate | ~13.6% | Utility Dive / Paces (2026) [B] |

---

## Notes on Interpretation

**Ranges versus point estimates.** Many figures above are ranges. This reflects genuine uncertainty in the underlying research, not imprecision in the sources. Environmental footprints in particular depend on assumptions about grid carbon intensity, cooling technology, and hardware efficiency that vary substantially across deployments. Use the full range when presenting these figures, and be explicit about what assumptions drive the endpoints.

**Convergence as evidence.** The 40–60% hidden-cost figure appears independently in Gartner analysis and Meta-Intelligence meta-analysis. This convergence strengthens the evidential basis: two methodologically distinct analyses reaching similar conclusions is more informative than a single figure from a single source.

**The 95% no-P&L figure.** The finding that approximately 95% of GenAI pilots produce no measurable profit-and-loss impact (MIT NANDA 2025) is striking and frequently contested. It does not mean that 95% of AI deployments are worthless — it means that the measurement infrastructure to attribute P&L impact to AI pilots is largely absent. This is a measurement failure as much as a deployment failure, and it reinforces the case for the measurement discipline described in [Measurement Discipline](../methodology/measurement-discipline.md).

**The McKinsey and Gartner figures.** These figures appear together because they represent the extremes of the current AI business discourse: McKinsey's $2.6–4.4 trillion annual economic value estimate is often cited to justify AI investment; Gartner's agentic-AI abandonment forecast is cited as a corrective. Neither is wrong, but neither is sufficient without the full-lifecycle cost analysis this framework provides. High potential value and high abandonment rates are not contradictory — they describe an investment landscape with large upside and poor average execution.

---

## Sources

- [A] Oil & Gas IQ, "Why Most AI Pilots in Oil and Gas Still Fail to Scale" (8 Jun 2026); figures from the *AI in Energy Summit 2026 Insights Report* (survey of 130+ energy leaders). Figures are self-reported or summit-survey-derived.
- [B] Utility Dive (sponsored by Paces), "How AI fits in the energy development workflow," K. Baranko (22 Jun 2026). Sponsored content.
- Anyreach (2026). *The Hidden Costs of AI in Business.* Industry analysis.
- Meta-Intelligence (2025). *State of AI in Business 2025.* Meta-analysis.
- MIT NANDA (2025). *The GenAI Divide: State of AI in Business 2025.*
- MIT Sloan Management Review (via Meta-Intelligence 2025). Enterprise AI value quantification survey.
- MIT News (2025). Data-centre water consumption. `[VERIFY]`
- ScienceDirect (2025). AI environmental footprint estimates. `[VERIFY specific article citation]`
- McKinsey Global Institute. GenAI economic value estimate. `[VERIFY edition and date]`
- Gartner (2024). Agentic AI enterprise adoption forecast. `[VERIFY]`
