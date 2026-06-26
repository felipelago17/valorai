# ValorAI — Measuring the True Financial Value of AI

## The Core Question

*Does the method measurably improve judgement under uncertainty?*

That question, drawn from Douglas Hubbard's work on evidence-based measurement in project management, is the framing question for everything in this repository. It is not rhetorical. Every valuation model, every cost taxonomy, every organisational recommendation must be held against it. A method that produces confident-looking numbers without improving actual decisions is not rigorous — it is an **analysis placebo**: process that raises certainty without raising accuracy.

ValorAI exists because most AI valuation practice fails that test. Organisations routinely compute return-on-investment figures that omit 40–60% of true costs, benchmark against productivity gains that evaporate under close inspection, and report strategic progress while only 13% of enterprises can quantify any measurable business value from their AI investments at all. The gap between rhetoric and evidence is not a communications problem. It is a measurement problem.

---

## What This Framework Does

ValorAI provides:

1. **An indirect-cost taxonomy** — seven categories of costs that are systematically excluded from standard AI business cases, with literature evidence for each. Hidden costs routinely equal or exceed visible subscription and compute spend.

2. **A valuation methodology** anchored in Hubbard's evidence-not-ritual discipline — total cost of ownership (TCO), ROI/NPV/IRR with full-lifecycle line items, real-options treatment of uncertainty, and value-of-information analysis to decide when more measurement is worth its cost.

3. **An evidence base** — a base-rate table of key quantitative findings and an annotated bibliography, so that every claim in the framework can be traced to a primary source.

4. **A use-case library** (in progress) — worked examples applying the methodology to real deployment decisions.

---

## Why Indirect Costs Are the Problem

When an organisation evaluates an AI tool, it typically sees:

- Licence or API subscription fees
- Initial implementation and training costs
- Projected efficiency gains (often vendor-supplied)

What it typically does not see:

- The ongoing maintenance burden that machine-learning systems accumulate over time — boundary erosion, data-dependency debt, model drift, hidden feedback loops
- Integration costs that, on average, expand total project cost by 2–3× beyond initial budget
- The verification overhead required to validate AI outputs before acting on them
- Cognitive effects: deskilling, automation bias, and the slow erosion of the tacit organisational judgement that the original ROI model assumed would persist
- Environmental costs — energy, water, land, e-waste — increasingly subject to carbon pricing and disclosure regulation
- Hidden labour: the annotation, moderation, and reinforcement-learning micro-work performed by low-wage workers in distributed supply chains
- Shadow AI: the approximately 90% of workers who use personal AI tools outside organisational governance, carrying data-leakage and compliance exposure that never appears on the IT budget

The thesis of this framework is simple: **a valuation that ignores these costs does not underestimate AI's cost — it mischaracterises the decision entirely.**

---

## How to Use This Site

| Section | Purpose |
|---|---|
| [Measurement Discipline](methodology/measurement-discipline.md) | The Hubbard methodological anchor; why evidence matters more than process |
| [Valuation Models](methodology/valuation-models.md) | TCO, ROI/NPV/IRR, real options, value-of-information |
| [Indirect Costs](indirect-costs/index.md) | Seven-category taxonomy with literature evidence |
| [Base Rates](evidence/base-rates.md) | Key quantitative findings in citable table form |
| [Bibliography](evidence/bibliography.md) | Annotated reference list |
| [Use Cases](use-cases/index.md) | Applied examples (forthcoming) |

---

## A Note on Epistemic Standards

This framework makes quantitative claims. Every figure cited here is sourced; where sources disagree or where estimates carry wide uncertainty bands (as environmental figures often do), this is stated explicitly. References marked `[VERIFY]` are included because the underlying finding is important, but independent verification of the specific citation is advised before relying on it in a published document.

No claim in this repository should be presented to a decision-maker without checking the source. The goal is not to produce confident-looking outputs — it is to improve the quality of decisions.
