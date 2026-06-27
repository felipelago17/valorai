# Field Evidence: The Pilot-to-Production Value Gap

## Overview

AI deployment literature frequently conflates two distinct phenomena: the technical success of a model and the operational realisation of business value. Evidence from the energy sector — one of the most data-rich and capital-intensive industries deploying AI at scale — illustrates sharply why the gap between the two is the central problem in AI valuation, not a footnote to it.

The figures on this page are drawn from a survey of 130+ energy leaders (AI in Energy Summit 2026 Insights Report) and from a June 2026 analysis of AI adoption patterns in energy development workflows. Both sources are practitioner-facing; figures are self-reported or summit-survey-derived and should be read as directional rather than independently audited.

---

## The 95% Figure: An Operational Failure, Not a Technical One

Survey evidence from the energy sector finds that up to **95% of AI initiatives still fail to deliver measurable value** [A]. The cause is not model performance. AI systems frequently perform well in controlled pilot environments — the data is curated, the teams are dedicated, and executive attention is sustained. The failure occurs in the transition to production, where data is messier, workflows are entrenched, and the sustained attention required for adoption dissipates.

This is the same finding reported by MIT NANDA across industries (approximately 95% of GenAI pilots with no measurable P&L impact; see [Base Rates](base-rates.md)). The energy-sector evidence adds a specific characterisation: the failure is **operational**, not algorithmic. The models work. The organisations do not scale them.

For AI valuation purposes, this matters because it reframes the risk. The question is not "will the model perform?" — that can be tested in a pilot. The question is "will the organisation embed the model into the workflows and decision processes through which value is actually generated?" That question cannot be answered by model evaluation alone.

---

## "POC Graveyards" and Innovation Theatre as an Indirect Cost

Energy practitioners identify a named pattern: the **"POC graveyard"**, also described as **innovation theatre** [A]. Pilots are initiated, they demonstrate value on controlled data, they generate internal momentum — and then they stall. No defined path to production exists. The pilot's success metrics (model accuracy, task completion in a test environment) do not translate to production performance measures. The initiative exhausts its budget and organisational attention without generating sustained value.

This is a distinct indirect-cost category in the ValorAI framework. The costs are:

- **Sunk pilot spend** — engineering, infrastructure, and management time invested in a deployment that never reaches production scale.
- **Opportunity cost** — the alternative uses of that capital and organisational attention that were forgone.
- **Change fatigue** — organisations that have cycled through multiple failed pilots develop resistance to new AI initiatives, raising the cost of future adoption. This is an organisational-capital cost that is structurally analogous to the cognitive and human-capital erosion described in [Cognitive & Human Capital](../indirect-costs/cognitive-human-capital.md).

A rigorous AI business case must include an explicit estimate of the probability that a given pilot will reach production scale — and apply that probability to the projected benefits before computing ROI. Treating pilot success as equivalent to deployment success is a category error that systematically inflates projected returns.

---

## The Value-Realisation Gate: Embedded vs. Dashboard AI

Survey evidence identifies a specific mechanism by which AI fails to generate value even after apparent deployment success: **placement in an analytics layer rather than in operational workflows** [A].

AI tools that deliver outputs to dashboards, reports, or analytics interfaces — but that do not directly enable frontline decisions — rarely generate the value projected at procurement. The chain from insight to action is broken. By contrast, AI that is embedded into the specific moment at which a decision is made — predictive maintenance that triggers a work order, a site-screening tool that produces a ranked list the next analyst step acts on — generates ROI because it removes friction from the decision itself.

This distinction defines a **value-realisation gate** in the ValorAI framework. Benefits projected in an AI business case are conditional on the AI being embedded at the decision point, not merely deployed to an analytics layer. Valuations should explicitly score the intended deployment mode and discount projected benefits accordingly.

Recommended embedding-depth scoring:

| Embedding level | Description | Benefit realisation weight |
|---|---|---|
| Dashboard / analytics layer | Outputs available for review; no direct workflow integration | Low (0.1–0.3×) |
| Workflow-embedded | Outputs surface within the tool or process where decisions occur | Moderate (0.5–0.7×) |
| Action-enabling | AI output directly triggers or enables the next operational step | Full (0.9–1.0×) |

These weights are illustrative starting points, not calibrated coefficients. They should be revised based on observed adoption rates in the specific organisational context.

---

## Scaling Barriers: Three Recurring Patterns

The survey of 130+ energy leaders identifies three barriers that account for the majority of pilot-to-production failures [A]:

### 1. Data Trust Gap
Approximately **30% of leaders cite data quality, foundations, and governance as the primary barrier to execution** [A] — the single most-cited factor. AI systems in production require a minimum accuracy threshold of approximately **85%** to establish and sustain operational trust [A]; below that threshold, frontline users stop relying on outputs and the value of deployment collapses.

Importantly, leading operators do not treat the data trust gap as a prerequisite to be resolved before deployment. They deploy on "good enough" data and improve it continuously in parallel, calibrating the deployment scope to the accuracy level the current data supports [A]. This is consistent with the ValorAI [Measurement Discipline](../methodology/measurement-discipline.md) principle: reduce uncertainty iteratively, do not wait for certainty before acting.

### 2. Workflow Embedding
Value is only realised when AI is embedded in daily decision-making, not when it exists as a parallel analytics capability [A]. The integration overhead required to achieve genuine workflow embedding — connecting AI outputs to the specific tools, roles, and processes through which work gets done — is consistently underestimated. This is the same cost dynamic documented in [Integration & Implementation](../indirect-costs/integration-implementation.md).

### 3. Workforce Readiness
Only **17% of surveyed energy organisations report being highly prepared for AI**, meaning their systems are embedded into daily workflows and their staff are AI-fluent [A] (self-reported, survey of 130+ energy leaders). The remaining 83% are in early or transitional stages. The binding constraint is not the availability of AI specialists — it is the AI fluency of the existing workforce. Skills gaps, change fatigue from repeated failed initiatives, and the loss of institutional knowledge as experienced staff disengage from AI-disrupted processes all compound the scaling barrier [A].

This aligns with the [Cognitive & Human Capital](../indirect-costs/cognitive-human-capital.md) analysis in ValorAI: workforce readiness is an organisational capital cost, not a training-budget line item.

---

## Sector-Level Context: Energy Development Workflows

For additional grounding, analysis of AI adoption in energy development (Utility Dive / Paces, June 2026) provides a workflow-level view of where value concentrates [B]:

**Sector adoption rate.** Energy and utilities AI adoption stands at approximately **13.6%** [B] — among the lowest across major industries — despite the sector's data richness and analytical history. This low baseline is context for interpreting both the 17% readiness figure and the 95% failure rate: the majority of the sector has not yet reached the point where these dynamics apply at scale.

**Jurisdiction-specificity as a constraint.** Energy development is deeply jurisdiction-specific: interconnection queue rules, permitting timelines, and grid operator requirements vary by geography in ways that generic AI tools cannot accommodate [B]. This specificity limits the transferability of AI deployments and raises the effective integration cost for each new operational context.

**Where value concentrates.** Workflow analysis identifies four areas where AI delivers demonstrable value in energy development [B]:

| Workflow | AI contribution |
|---|---|
| Site search & origination | Ranked site lists generated in minutes rather than days |
| Site triage & prioritisation | Reduction of large candidate sets (e.g. 500 sites) to actionable shortlists |
| Project tracking | Automated monitoring of permitting documents, deadlines, and timelines |
| Community sentiment research | Structured diligence reports for stakeholder engagement |

The recommended entry point is the **highest-volume, most repetitive workflow** — site screening and triage — rather than the most analytically sophisticated one [B]. Human judgement is retained for final decisions, relationship management, and locally-informed calls. This is consistent with the action-enabling embedding model: the AI reduces the volume of work a human must do, rather than replacing the human at the decision point.

---

## Upper-Bound Benchmark

Some operators in the energy sector report **over $150 million in recurring value** from scaled AI deployments [A] (self-reported by operators; not independently audited). This figure is included as an upper-bound benchmark anchor, not as a typical outcome. The distribution of outcomes is heavily skewed: a small proportion of deployments achieve large-scale value, while the majority — consistent with the 95% figure — do not reach production scale at all.

The appropriate use of this benchmark in a business case is as a ceiling on the optimistic scenario, paired with the 95% base-rate probability of not reaching that ceiling.

---

## Sources

[A] Oil & Gas IQ, "Why Most AI Pilots in Oil and Gas Still Fail to Scale" (8 Jun 2026); figures from the *AI in Energy Summit 2026 Insights Report* (survey of 130+ energy leaders). Figures are self-reported or summit-survey-derived.

[B] Utility Dive (sponsored by Paces), "How AI fits in the energy development workflow," K. Baranko (22 Jun 2026). Sponsored content; workflow-level analysis from a vendor perspective.
