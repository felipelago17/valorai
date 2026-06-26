# Technical & Operational Debt

## Definition

Technical debt — the deferred cost of expedient engineering decisions — is a familiar concept in software development. Machine learning systems accumulate a distinct and more severe variant. Sculley and colleagues (2015) identified at NeurIPS that the interaction between ML components and the broader software environment generates maintenance obligations that dwarf those of conventional software, and that these obligations are largely invisible at the point of deployment.

The term they introduce — **hidden technical debt in machine learning systems** — captures an important phenomenon: the debt is not merely deferred, it is often unrecognised until it has compounded substantially.

## The Evidence

Sculley et al. identify several mechanisms by which ML systems accumulate maintenance debt:

**Boundary erosion.** A model trained on data from system A will be consumed by system B, which was not part of the original design. Over time, these undeclared dependencies proliferate. When system A changes — when its data schema is updated, its API is revised, or its business logic shifts — the consuming model breaks in ways that are difficult to trace and expensive to repair.

**Entanglement.** Changing any input feature to an ML model changes the model's entire behaviour, because features interact in ways that are not decomposable. The consequence is that improvements to one part of the system create unexpected regressions elsewhere. The CACE principle — **Change Anything, Change Everything** — means that routine maintenance carries systemic risk.

**Hidden feedback loops.** When an ML system's outputs influence the data it is later trained on, the system begins to shape its own future behaviour. These feedback loops are often invisible to the teams operating the system and can cause behaviour that diverges significantly from what was observed at deployment.

**Undeclared consumers.** As ML systems become reliable, other systems are built on top of them without formal dependency management. The original system cannot be changed without breaking consumers whose existence is unknown.

**Data-dependency debt.** ML systems are tightly coupled to the characteristics of their training data. When data sources change — as they inevitably do in production environments — models silently degrade. The cost of detecting, diagnosing, and remedying data drift is ongoing.

**Configuration debt.** The hyperparameters, preprocessing steps, and pipeline configurations that determine a model's behaviour are often poorly documented, replicated without review, and difficult to audit. Small configuration errors can have large effects.

**Model drift and retraining.** All deployed models degrade over time as the statistical distribution of incoming data diverges from training data. Retraining is not a one-time cost — it is a recurring operational obligation.

## What the Costs Look Like in Practice

The aggregate effect of these mechanisms is that the total maintenance cost of a production ML system typically exceeds its initial construction cost within 12–18 months of deployment. A system that required six months of engineering effort to build may require ongoing engineering investment at a rate that makes the original effort look modest.

This has an important implication for AI valuations that project benefits over multi-year horizons: the denominator (cost) grows over time in ways that the numerator (benefit) may not. A positive-NPV investment in year one can become a negative-NPV obligation by year three if maintenance costs are not modelled explicitly.

## How This Enters the Valuation

Technical and operational debt should appear in the TCO model as:

- **Annual retraining cost** — compute, data-engineering time, and model-evaluation overhead, recurring.
- **Monitoring and drift-detection tooling** — infrastructure cost for observing model behaviour in production.
- **Maintenance engineering allocation** — a fraction of ongoing engineering capacity that cannot be directed to new work.
- **Incident response provision** — budget for diagnosing and remediating the model failures that will occur.

A conservative starting estimate is that ongoing ML maintenance requires engineering effort equivalent to 20–30% of the original build effort, annually. This figure should be revised upward for systems with many consumers, high data-change rates, or direct decision-making authority.

---

## References

- Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J. F. & Dennison, D. (2015). *Hidden Technical Debt in Machine Learning Systems.* Advances in Neural Information Processing Systems 28 (NeurIPS 2015), pp. 2503–2511.
