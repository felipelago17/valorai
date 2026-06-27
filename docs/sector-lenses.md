# Sector Lenses

_Last reviewed: 2026-06-27_

## What sector lenses are — and are not

Each sector tends to distribute AI's indirect costs differently across the [seven-category taxonomy](indirect-costs/index.md). A regulatory-intensive sector like financial services bears a disproportionate verification and governance burden; an OT-heavy sector like energy bears a disproportionate integration and technical-debt burden; knowledge-work sectors bear the highest cognitive-skills and shadow-AI exposure.

The table below captures these tendencies as **directional priors**: qualitative signals about which cost categories deserve the most attention in a given context. They are starting hypotheses to be tested against the [base-rate evidence](evidence/base-rates.md) and the specific facts of a deployment — not coefficients to multiply against a visible cost figure.

!!! warning "These are attention priors, not arithmetic multipliers"
    No cell in the matrix below should be converted to a decimal and multiplied against a cost line.
    Any quantitative adjustment derived from this table must be expressed as an explicit range with
    stated assumptions, and must be grounded in the [base-rate evidence](evidence/base-rates.md) or
    a cited primary source. A precise-looking sector multiplier would itself be an analysis placebo.

---

## Weighting matrix

*Weights: **VH** = Very High · **H** = High · **M** = Medium · **L** = Low*

Column abbreviations follow the exact category names used throughout this site.

| Sector | Tech & Op Debt | Integration | Verification | Cognitive & Human Capital | Environmental | Labour & Supply Chain | Governance & Shadow AI |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [Energy & Utilities](#energy--utilities) | **H** | **H** | **H** | M | M–H | M | L–M |
| [Financial Services](#financial-services) | M | **H** | **VH** | M–H | L–M | M | **H** |
| [Healthcare & Life Sciences](#healthcare--life-sciences) | M | **H** | **VH** | **H** | L–M | **H** | M |
| [Legal / Compliance / Prof. Services](#legal--compliance--professional-services) | L–M | M | **VH** | **H** | L | M | **H** |
| [Manufacturing & Industrials](#manufacturing--industrials) | **H** | **H** | M–H | M | M | M | L–M |
| [Knowledge Work (cross-sector)](#knowledge-work-cross-sector) | M | M | **H** | **H** | L–M | M | **VH** |

---

## Per-sector rationale

### Energy & Utilities

**Technical & Operational Debt — H.** OT/SCADA environments frequently run 20–40-year-old infrastructure. AI systems connecting to legacy historians, PLCs, or DCS platforms create data-dependency debt and boundary erosion in the sense established by Sculley et al. (2015). Model drift is endemic where process conditions vary seasonally and equipment degrades non-linearly. Expect ongoing maintenance overhead from the first year of production.

**Integration & Implementation — H.** OT/IT convergence requires crossing air gaps, proprietary protocols (OPC-UA, Modbus, HART), and safety-instrumented system (SIS) interfaces. Brownfield complexity is the primary cost driver, not the AI platform itself. The Energy sector's 95% initiative-failure rate (AI in Energy Summit 2026) and 17% high-preparedness rate are consistent with integration underestimation as a primary mechanism. `[VERIFY: OT/AI integration overrun studies for energy sector specifically]`

**Verification & Oversight — H.** Safety-critical operations require human-in-the-loop for every actionable alert. Health, safety, and environment (HSE) regulatory requirements and documented alert-fatigue risk in industrial AI mean that verification overhead is structurally unavoidable in this sector. See [Verification & Oversight](indirect-costs/verification-oversight.md). `[VERIFY: sector-specific verification overhead studies]`

**Cognitive & Human Capital — M.** Maintenance technicians risk gradual loss of diagnostic intuition, consistent with the cognitive offloading mechanism documented by Lee et al. (2025) and Kosmyna et al. (2025). Physical safety and hands-on operational requirements partially mitigate this compared with purely knowledge-work contexts. `[VERIFY: energy/industrial maintenance deskilling evidence]`

**Environmental Externalities — M–H.** The IEA's *Energy and AI* (2025) projects data-centre demand doubling to ~945 TWh by 2030. Edge-computing and cloud inference loads compound an already energy-intensive sector. Freshwater exposure documented by Li et al. (2023) applies to cooling-intensive data centres hosting energy-sector AI. The sector is under intensifying disclosure pressure (TCFD, SEC climate rules). See [Environmental Externalities](indirect-costs/environmental-externalities.md).

**Labour & Supply Chain — M.** Sensor-anomaly annotation and model-training data are typically outsourced; workforce transition costs accrue if maintenance roles are partially automated. See [Labour & Supply Chain](indirect-costs/labour-supply-chain.md). `[VERIFY: energy sector annotation supply chain specifics]`

**Governance & Shadow AI — L–M.** OT environments have limited personal-device access, reducing shadow AI exposure compared with knowledge-work sectors. However, field-based AI tools and engineering workstations are an emerging vector. JV governance (IP ownership of trained models, cross-partner data sharing, export-control implications of operational data) is a non-trivial governance overhead in multi-partner deployments.

---

### Financial Services

**Verification & Oversight — VH.** Model risk management (MRM) frameworks — equivalent to SR 11-7 in the US, EBA guidelines in the EU — mandate validation, back-testing, and explainability requirements for credit, market, and operational-risk models. Regulatory expectations for AI-assisted decisions in lending and sanctions screening are stringent and intensifying. `[VERIFY: current supervisory guidance references by jurisdiction]`

**Integration & Implementation — H.** Core banking system integration (Temenos, FIS, Finastra, COBOL-based mainframes) is notoriously complex. API layers reduce but do not eliminate integration risk. `[VERIFY: financial services AI integration overrun studies]`

**Cognitive & Human Capital — M–H.** Analyst and underwriter deskilling risk is consistent with Dell'Acqua et al.'s (2023) jagged-frontier finding — AI-reliant professionals underperform peers on tasks outside AI's competence boundary. Cognitive offloading in compliance screening is documented by Lee et al. (2025).

**Governance & Shadow AI — H.** Knowledge workers in financial services are among the heaviest personal-AI users. MIT NANDA (2025) reports ~90% of workers use personal AI tools; client confidentiality and data-privacy obligations (GDPR, CCPA, financial secrecy rules) make shadow-AI exposure a material compliance risk.

---

### Healthcare & Life Sciences

**Verification & Oversight — VH.** Every AI-assisted diagnosis or treatment recommendation requires clinician review. FDA clinical AI regulations, EU MDR for AI medical devices, and the automation-bias literature (Parasuraman & Manzey 2010) converge on the conclusion that verification overhead in clinical AI is both mandatory and substantial.

**Cognitive & Human Capital — H.** Healthcare is the sector with the most specific evidence of AI-induced deskilling. Natali et al. (2025) document measurable declines in independent diagnostic accuracy among AI-reliant clinicians. Patient safety implications make this the most consequential deskilling risk in any sector. See [Cognitive & Human Capital](indirect-costs/cognitive-human-capital.md).

**Integration & Implementation — H.** HL7/FHIR integration with EHR systems (Epic, Cerner), PACS imaging data, and laboratory information management systems creates layered integration complexity. `[VERIFY: healthcare AI integration overrun studies]`

**Labour & Supply Chain — H.** Medical data annotation (radiology labels, pathology slides, clinical text) is specialised and carries supply-chain risk. Patient data protection requirements (HIPAA, GDPR Article 9) mean annotation errors carry direct liability exposure. See [Labour & Supply Chain](indirect-costs/labour-supply-chain.md).

---

### Legal / Compliance / Professional Services

**Verification & Oversight — VH.** Legal accuracy requirements are absolute in many contexts: an incorrect citation, an omitted clause, or a hallucinated precedent creates professional liability. Dell'Acqua et al. (2023) empirically identify the "jagged frontier" — the boundary of tasks where AI performs well versus poorly — and show that professionals who trust AI uniformly perform worse on tasks in the poor-performance zone. See [Verification & Oversight](indirect-costs/verification-oversight.md).

**Cognitive & Human Capital — H.** Junior lawyer training, document-review atrophy, and the erosion of adversarial research instincts are documented concerns in the legal profession. Lee et al. (2025) survey (319 knowledge workers) and Kosmyna et al. (2025) EEG study both support the cognitive offloading mechanism. See [Cognitive & Human Capital](indirect-costs/cognitive-human-capital.md).

**Governance & Shadow AI — H.** Legal professionals are heavy personal AI users for drafting and research. Client confidentiality, conflict-checking obligations, and privilege considerations are absent from consumer AI tools. MIT NANDA's (2025) shadow AI economy finding applies with particular force here.

---

### Manufacturing & Industrials

**Technical & Operational Debt — H.** Manufacturing AI on legacy PLCs and SCADA systems creates OT-debt dynamics similar to Energy. Production process variation and equipment degradation drive persistent model drift. Sculley et al.'s (2015) ML-debt taxonomy applies directly.

**Integration & Implementation — H.** ERP (SAP S/4HANA), MES, and OT integration creates a three-layer complexity stack. ISO 55000 asset management compliance adds documentation overhead. `[VERIFY: manufacturing AI integration overrun studies]`

**Labour & Supply Chain — M.** Acemoglu & Restrepo (2022) empirically link task automation to wage inequality and displacement concentrated in routine-task-intensive roles — a finding directly applicable to manufacturing. See [Labour & Supply Chain](indirect-costs/labour-supply-chain.md).

---

### Knowledge Work (cross-sector)

**Governance & Shadow AI — VH.** MIT NANDA's (2025) finding that ~90% of workers use personal AI tools applies most forcefully in office and knowledge-work contexts, where personal devices are universal and organisational oversight is weakest. Sensitive data in personal AI tools, IP leakage, and AI-generated content in unaudited work products are the primary exposure vectors. See [Governance & Shadow AI](indirect-costs/governance-shadow-ai.md).

**Cognitive & Human Capital — H.** The most extensively documented deskilling risk. Lee et al. (2025) show that higher AI trust is associated with reduced independent critical effort in a survey of 319 knowledge workers (936 examples). Kosmyna et al. (2025) show reduced neural engagement and weaker recall in LLM-assisted writing. The mechanism is continuous and cumulative, not episodic. See [Cognitive & Human Capital](indirect-costs/cognitive-human-capital.md).

**Verification & Oversight — H.** Dell'Acqua et al.'s (2023) jagged-frontier finding establishes that knowledge workers using AI uniformly — without active verification of AI's competence boundary — underperform peers on tasks outside that boundary. The verification overhead required to avoid this is structurally high in knowledge work.

---

## From qualitative priors to quantitative ranges

When moving from this matrix to a financial model, the appropriate procedure is:

1. **Identify the H/VH categories** for the relevant sector.
2. **Consult the [base-rate table](evidence/base-rates.md)** for empirical anchor points (e.g. the 40–60% hidden-cost aggregate, the 2–3× integration cost expansion).
3. **Express each category as a range**, not a point estimate, with an explicit assumption statement (e.g. "integration overrun: 30–50% of the integration build cost, assuming brownfield OT environment; reduce if greenfield").
4. **Cite the evidence** or mark the assumption `[VERIFY]` if ungrounded.
5. **Sum the ranges** — the full TCO range will be wide; that width is informative, not a modelling failure.

See the [Energy: Predictive Maintenance use case](use-cases/energy-predictive-maintenance.md) for a worked example applying this procedure to an Energy & Utilities deployment.

---

## Cross-portfolio connections

The sector lenses in this page intersect directly with the companion repositories in this research programme:

- **Compliance costs in AI adoption** are highest in Financial Services and Legal — sectors where export-control and sanctions classification of AI models adds a further regulatory-cost layer. See *[Sanctions & Export Controls — AI and Oil](https://felipelago17.github.io/Sanctions-and-Export-Controls-AI-and-Oil/)* for the verification and governance cost that frontier-model adoption under dual-use regimes entails.

- **The verification and governance rows** in this matrix map directly onto the control crosswalks in *[Responsible AI Evaluation](https://felipelago17.github.io/Responsible-AI-evaluation/)* (NIST AI RMF, EU AI Act, ISO 42001). ValorAI provides the measurement engine; Responsible AI Evaluation provides the control framework. The two are designed to be used together.

- **Regulatory-change signals** that shift the verification or governance cost burden — new supervisory guidance, new sector-specific AI regulations, enforcement actions — are tracked in *[AI Regulatory Monitor](https://felipelago17.github.io/AI-regulatory-monitor/)*. Feed those signals into the H/VH cells most affected.

- **JV structures in the Energy sector** introduce a governance dimension that single-operator analysis omits: which partner bears which indirect cost, how model IP is owned, and how data sovereignty is maintained across JV boundaries. See *[Joint Ventures & the Energy Trilemma](https://felipelago17.github.io/Joint-ventures-and-Energy-Trilemma-/)* for the governance framework.

---

## Evidence references

| Finding | Source |
|---|---|
| Cognitive offloading in knowledge workers | Lee et al. (2025), CHI '25 — [Literature](literature/bibliography.md) |
| Neural engagement / cognitive debt | Kosmyna et al. (2025), arXiv:2506.08872 — [Literature](literature/bibliography.md) |
| Jagged technological frontier | Dell'Acqua et al. (2023), HBS WP 24-013 — [Literature](literature/bibliography.md) |
| AI-induced deskilling in medicine | Natali et al. (2025), *AI Review* 58:356 — [Bibliography](evidence/bibliography.md) |
| Automation complacency and bias | Parasuraman & Manzey (2010), *Human Factors* 52(3) — [Bibliography](evidence/bibliography.md) |
| ML technical debt taxonomy | Sculley et al. (2015), NeurIPS 28 — [Bibliography](evidence/bibliography.md) |
| Shadow AI economy | MIT NANDA (2025) — [Literature](literature/bibliography.md) |
| Task automation and wage inequality | Acemoglu & Restrepo (2022), *Econometrica* 90(5) — [Literature](literature/bibliography.md) |
| Energy data-centre demand growth | IEA *Energy and AI* (2025) — [Literature](literature/bibliography.md) |
| Inference energy and carbon intensity | Luccioni, Jernite & Strubell (2024), FAccT '24 — [Literature](literature/bibliography.md) |
| AI water footprint | Li et al. (2023), arXiv:2304.03271 — [Literature](literature/bibliography.md) |
| Energy sector pilot failure rate | AI in Energy Summit 2026 — [Evidence](evidence/energy-pilot-gap.md) |
