# Integration & Implementation

## Definition

The integration cost of an AI system is the cost of connecting that system to the organisational context in which it must function: existing data infrastructure, operational workflows, governance processes, and the human roles that interact with it. It is distinct from the cost of the AI system itself, and in most deployments it is larger.

The distinction matters because integration costs are largely invisible at procurement. A vendor's pricing and ROI calculator are scoped to the system, not to the organisational work required to make the system useful. That work falls on the buyer.

## The Evidence

Independent analysis of AI project outcomes consistently finds that total project costs expand by **2–3× beyond initial budget**, and that the primary driver of this expansion is integration complexity that was not scoped at the outset (Anyreach 2026; Meta-Intelligence 2025).

The 2–3× figure is a base-rate expectation, not a worst-case outcome. It reflects the systematic underestimation of integration work that occurs when organisations scope AI projects using vendor estimates, analogise from their experience with conventional software procurement, or rely on integration timelines supplied by parties whose incentives favour optimism.

Several specific mechanisms drive overruns:

**Data readiness gaps.** AI systems require data that is clean, labelled, accessible, and representative. In most organisations, data that satisfies these requirements does not pre-exist — it must be created. Data preparation and data engineering work is routinely the largest single cost category in AI implementations, and it is routinely underestimated.

**API and system integration complexity.** Connecting an AI system to legacy enterprise systems (ERP, CRM, data warehouses, operational databases) involves interface engineering, authentication, data-format translation, and error-handling that accumulates far beyond what preliminary technical assessments suggest.

**Process redesign.** The productivity gains projected at procurement assume that existing workflows will be modified to incorporate AI outputs. In practice, workflow redesign is a change-management challenge, not a technical one, and it takes longer and costs more than technical estimates capture.

**Build-versus-buy dynamics.** Organisations that elect to build AI capabilities internally rather than procure them externally face a compounding problem: internal builds stall at approximately three times the rate of externally-integrated systems, and the primary reason is underestimated integration complexity (Anyreach 2026). The "build" option is frequently chosen because it appears to offer cost savings and control; it frequently delivers neither.

**Scope expansion.** Once an AI integration project begins, stakeholders identify adjacent use cases and request extensions. Scope expansion is not unique to AI projects, but the technical dependencies of ML systems — particularly the data-dependency debt described in [Technical Debt](technical-debt.md) — mean that scope expansion in AI projects is disproportionately costly.

### Cross-sector prior: IT project overruns

The AI-specific 2–3× cost expansion finding (Anyreach 2026) sits within a well-documented general pattern. Flyvbjerg & Budzier (2011) analysed a large cross-sector dataset of IT projects and found that cost overruns follow a **fat-tailed distribution** — the finding that matters most is not the mean (~27% overrun) but the tail: roughly **1 in 6 IT projects becomes a "black swan"**, exceeding 200% cost overrun and 70% schedule overrun. `[VERIFY exact figures against article]`

The Standish Group *CHAOS Reports* provide directional corroboration: historically, only 29–42% of software projects meet their original cost, schedule, and scope objectives; 40–50% are "challenged"; 18–25% are outright failures. `[METHODOLOGICALLY DEBATED — sampling and success criteria not fully disclosed; use as directional, triangulated with Flyvbjerg & Budzier]`

These cross-sector results are the baseline from which sector-specific AI integration adjusters should bend:

- **Energy (brownfield OT/SCADA):** integration overrun risk is at the upper end of — or above — the cross-sector distribution. `[VERIFY: sector-specific OT/AI integration overrun studies]`
- **Financial services (core banking):** complex legacy interfaces (COBOL mainframes, Temenos, FIS) push toward the upper end. `[VERIFY: financial services AI integration overrun studies]`
- **Healthcare (EHR/PACS):** HL7/FHIR integration complexity is well-documented as a high-overrun context. `[VERIFY: healthcare AI integration overrun studies]`
- **Manufacturing (ERP + OT):** three-layer complexity (ERP/MES/OT) compounds the cross-sector risk. `[VERIFY: manufacturing AI integration overrun studies]`

The sector `[VERIFY]` flags above are intentional: the cross-sector prior is established; the sector-specific bend is where additional research is needed before citing a specific multiplier.

## How This Enters the Valuation

Integration and implementation costs should be treated as follows in the TCO model:

- **Integration engineering** — estimated independently of vendor figures, based on the organisation's own assessment of data readiness, system complexity, and workflow-redesign scope.
- **Contingency for overrun** — given the 2–3× base rate, a minimum 50% contingency on the initial integration estimate is conservative. A more defensible approach is to model the overrun distribution explicitly and apply value-of-information analysis to determine whether additional scoping work is worthwhile before committing.
- **Ongoing integration maintenance** — connections between AI systems and upstream data sources degrade as those sources change. A recurring maintenance allocation is required.

A practical calibration: if the vendor's estimate of integration cost is X, the base-rate-informed estimate is 1.5X–2X for well-scoped projects and 2X–3X for projects where data readiness has not been independently assessed.

---

## References

- Anyreach (2026). *The Hidden Costs of AI in Business: What Your ROI Calculator Isn't Telling You.* — 2–3× cost expansion; build-vs-buy stall rate.
- Flyvbjerg, B. & Budzier, A. (2011). Why your IT project may be riskier than you think. *Harvard Business Review,* September 2011. — Fat-tailed IT overrun distribution; cross-sector prior. `[VERIFY exact figures]`
- Meta-Intelligence (2025). *State of AI in Business 2025.* — Independent convergence on 40–60% hidden cost share.
- Sculley, D. et al. (2015). *Hidden Technical Debt in Machine Learning Systems.* NeurIPS 28. — Data-dependency debt mechanisms.
- Standish Group. *CHAOS Reports* (periodic). — Software project outcome rates; directional prior. `[METHODOLOGICALLY DEBATED]`
