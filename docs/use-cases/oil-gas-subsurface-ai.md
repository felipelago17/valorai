# Oil & Gas: AI-Enabled Seismic Interpretation & Subsurface Characterisation

_Last reviewed: 2026-07-03_

!!! example "Illustrative worked example"
    All cost and benefit figures in this use case are **illustrative ranges** constructed to demonstrate the ValorAI methodology. They are not derived from a specific operator's data and must not be treated as benchmarks or forecasts. Where figures are grounded in the [base-rate evidence](../evidence/base-rates.md) or [literature](../literature/bibliography.md), this is indicated. Where they are not, they are marked `[VERIFY]` or labelled "illustrative assumption."

---

## 1. Context & Visible Costs

### Deployment scenario

A mid-tier independent E&P operator — or a subsidiary of a national oil company — is evaluating the transition from manual seismic interpretation workflows to an AI-assisted seismic interpretation platform across a portfolio of three to five basins. The trigger is a proof-of-concept (POC) on a single 3D survey that demonstrated accelerated horizon-picking throughput. The decision is whether to commit to an enterprise licence and full-portfolio rollout.

This scenario spans three distinct sub-contexts, each with a different value profile and governance footprint:

**Sub-scenario A — Exploration risk reduction.** AI is applied to frontier or near-field 3D seismic to identify structural and stratigraphic prospects, rank prospect inventories, and reduce the number of exploration wells drilled on low-confidence targets. The primary value driver is reduction in dry-hole rate; the primary hidden cost is the reserves-audit burden when AI-picked prospects advance toward a drilling decision.

**Sub-scenario B — Field development planning.** AI-assisted horizon tracking, fault interpretation, and seismic facies classification are used to constrain static reservoir models, reduce volumetric uncertainty (compress the P10–P90 spread), and accelerate time from seismic acquisition to final investment decision (FID). The primary value driver is accelerated FID and improved capex efficiency; the primary hidden cost is the cognitive deskilling of geoscientists who progressively delegate interpretation judgement.

**Sub-scenario C — Energy transition: subsurface CO₂ storage qualification.** AI tools derived from exploration workflows are repurposed to screen and characterise candidate CO₂ storage reservoirs (saline aquifers, depleted fields) for Carbon Capture, Utilisation and Storage (CCUS) projects. The primary value driver is compressed site-qualification timelines; the primary hidden costs are model generalisation failure (exploration training data is not necessarily representative of storage-relevant attributes) and heightened regulatory-audit requirements for storage-capacity certification. `[VERIFY: AI-specific CCUS site-qualification overrun studies]`

This context maps to the **Energy & Utilities** row of the [Sector Lenses](../sector-lenses.md#energy--utilities) matrix, with several cells elevated relative to the operational AI baseline used in the [Predictive Maintenance](energy-predictive-maintenance.md) case:

- **Verification** is elevated to Very High because AI-derived seismic interpretations that inform reserves estimates must satisfy a "reliable technology" standard for regulatory and financial reporting purposes.
- **Cognitive & Human Capital** is elevated to High because seismic interpretation is a highly skilled cognitive task with limited physical-safety backstop. Deskilling risk accumulates faster than in mixed cognitive/physical roles.
- **Governance** is elevated to High because seismic data is government-regulated in most producing nations, and reserves classification carries direct financial-reporting implications.

### Visible cost line items

All figures are illustrative ranges. `[VERIFY with current enterprise vendor pricing for seismic AI platforms]`

| Cost line item | Type | Illustrative range |
|---|---|---|
| AI seismic interpretation platform licence (enterprise, multi-basin) | Recurring | $300k–$900k / year |
| Cloud / HPC compute for ML seismic processing (GPU cluster or cloud burst) | Recurring | $150k–$500k / year |
| Seismic data curation and SEG-Y standardisation (one-off) | One-off capital | $100k–$350k |
| Geoscientist training and workflow integration (one-off) | One-off | $80k–$250k |
| Interpretation software integration (Petrel / Kingdom / RokDoc API build) | One-off capital | $100k–$300k |
| **Year-1 visible total** | — | **$730k–$2,300k** |
| **Ongoing visible (Years 2+)** | Annual | **$450k–$1,400k / year** |

!!! note "Basis for these ranges"
    Platform licence estimates reflect the enterprise tier of AI seismic interpretation products in the market (foundation models, multi-survey licences, QC tooling). `[VERIFY with current vendor pricing — Halliburton AI, CGG Insight, Ikon Science, SLB products]`. Compute costs for GPU-accelerated seismic ML processing are based on general cloud GPU pricing applied to a typical 3D survey workload; actual figures vary substantially with survey size and sampling density. `[VERIFY with GPU-hour estimates for representative survey sizes]`.

---

## 2. Framework Application

The seven indirect-cost categories are applied using the Energy & Utilities sector lens, adjusted upward where the subsurface interpretation context creates structurally higher exposure.

### Category 1: Technical & Operational Debt  *(Sector lens: High)*

Seismic datasets accumulated over decades of exploration are heterogeneous in ways that create significant data-dependency debt. Surveys acquired with different vintage equipment, processed with different migration parameters, or sampled at different temporal and spatial intervals resist direct model transfer: a CNN-based fault detector trained on North Sea post-stack time-migrated data will not generalise to pre-stack depth-migrated data from a geologically distinct basin without retraining. This is the CACE ("Changing Anything Changes Everything") principle from Sculley et al. (2015) applied to geophysical data rather than conventional software inputs.

The technical debt accumulates in two layers:

- **Dataset heterogeneity debt.** Every new basin onboarded to the platform requires data preparation work (format normalisation, phase calibration, polarity convention standardisation) before model transfer is reliable. This cost is invisible at the POC stage, when only one survey is in scope.
- **Model vintage debt.** As new seismic surveys are acquired (reprocessed vintages, 4D time-lapse surveys), existing models trained on earlier data must be retrained or at minimum re-validated. This is an ongoing maintenance obligation.

**Range (annual, ongoing):** $40k–$200k/year — estimated as 10–30% of platform licence, reflecting retraining and QC overhead. *Assumption: At the lower bound, models transfer well across the portfolio with light fine-tuning. At the upper bound, geological diversity across basins requires substantial per-basin customisation and the platform is heavily customised (on-premise or hybrid deployment). `[VERIFY with energy-sector ML maintenance cost studies]`*

### Category 2: Integration & Implementation  *(Sector lens: High)*

The seismic interpretation software ecosystem (Petrel, Kingdom, Ikon RokDoc, OpendTect, DecisionSpace) is not designed with open ML integration in mind. Connecting an AI interpretation platform to these workflows requires:

- Bidirectional SEG-Y and SEGY-P1 export/import bridges
- Horizon and fault pick file exchange (OMF, ASCII, XYZ formats)
- HPC or cloud job submission integration (PBS Pro, Slurm, AWS Batch)
- QC visualisation hooks into the interpreter's existing workstation
- Well-tie validation pipeline connecting interpreted horizons to checkshots and sonic logs

This integration layer is invisible in the vendor's POC demo, which typically runs on the vendor's pre-prepared dataset. In a production environment, the integration layer often costs more than the platform itself.

The 2–3× total-project-cost-expansion finding (Anyreach 2026) applies here: the $100k–$300k integration estimate in the visible cost line should be treated as a base from which the overrun distribution extends upward.

**Range (one-off overrun risk above visible integration budget):** $60k–$420k additional one-off. *Assumption: 30–70% additional cost on the integration build, reflecting OT-grade data pipeline complexity. The higher end applies when legacy interpretation packages require bespoke middleware or when the operator's data is held in a proprietary formation evaluation database with non-standard export paths. Grounded in the Anyreach (2026) 2–3× cost-expansion base rate and Flyvbjerg & Budzier (2011) fat-tail distribution for IT projects. `[VERIFY with seismic software integration cost studies specifically]`*

### Category 3: Verification & Oversight  *(Sector lens: Very High)*

This is the most structurally elevated cost category in the subsurface AI context, and it is almost entirely absent from vendor ROI models.

**The reserves-audit obligation.** E&P companies listed on major exchanges are required to report proved reserves using methodologies that meet a "reliable technology" standard — defined by the US SEC under Rules 4-10(a)(22) and globally referenced through SPE-PRMS guidelines. When seismic interpretation automated by an AI model becomes the basis for a reserves estimate, the model's methodology must be capable of being validated by a Qualified Reserves Evaluator (QRE). This requires:

- Documentation of training data provenance, labelling methodology, and validation hold-out results
- Explainability of model outputs (why this horizon at this location?) sufficient for a QRE to assess reliability
- Back-testing against wells drilled on AI-picked prospects (not available at POC stage)
- An auditable change log for model versions used in each reserves estimate

None of these requirements is automatic in a commercial AI seismic platform. They represent significant geoscientist and legal time to establish and maintain.

**The cognitive QC obligation.** AI-generated interpretations require skilled geoscientist QC before they enter a decision workflow. Alert fatigue in the seismic context manifests as acceptance of AI picks without adequate geological scrutiny — analogous to automation bias in clinical or industrial AI, but with direct consequences for drilling decisions worth tens to hundreds of millions of dollars.

**Range (annual, ongoing):** $80k–$300k/year — expressed as 0.5–2 FTE of senior geoscientist or reservoir engineer time, plus legal and audit overhead for reserves-compliant documentation. *Assumption: At the lower bound, the platform has strong built-in QC tooling, training data is well-documented, and reserves reporting scope is limited. At the upper bound, the operator is a listed company with SEC-reportable reserves covering multiple AI-interpreted surveys, requiring per-survey model validation documentation. `[VERIFY with QRE time allocation studies for AI-assisted reserves estimation]`*

### Category 4: Cognitive & Human Capital  *(Sector lens: High)*

Seismic interpretation is one of the most cognitively demanding and least-codified skills in the geosciences. An experienced interpreter reads seismic data the way a radiologist reads an MRI — through pattern recognition trained over years of practice, informed by geological knowledge that is not fully articulable. This tacit knowledge is precisely what AI interpretation systems are designed to replicate.

The deskilling risk operates on two timescales:

- **Individual deskilling.** Geoscientists who consistently delegate first-pass interpretation to AI progressively lose the interpretive intuition required to recognise when the AI is wrong. Gerlich (2025) finds a statistically significant negative correlation between AI tool use intensity and critical-thinking performance in general cognitive tasks. The mechanism — cognitive offloading — applies directly to geoscience interpretation, where the skills not exercised are the hardest to recover.
- **Organisational skill loss.** Junior geoscientists who have not developed manual interpretation skills cannot QC AI outputs as effectively as experienced interpreters. If senior interpreters retire and junior interpreters have developed primarily AI-assisted workflows, the organisation's ability to identify AI failure modes degrades.

This cost does not appear in Year 1 or even Year 2. It accumulates on a 3–7 year horizon and is expressed as a discount on the long-run productivity benefit projected at the time of investment.

**Range (expressed as a discount on long-run productivity projections):** 10–25% reduction in projected long-run productivity gain, applied from Year 3 onwards. *Assumption: At the lower bound, the operator maintains mandatory manual interpretation exercises for all geoscientists and invests in training programs that preserve interpretive skill. At the upper bound, no such programme exists and the platform becomes the primary first-pass interpretation tool within two years of deployment. `[VERIFY with longitudinal geoscience deskilling evidence — see NR.no subsurface AI research]`*

### Category 5: Environmental Externalities  *(Sector lens: Medium–High)*

Seismic ML processing is GPU-intensive in ways that make the environmental cost of AI subsurface workflows meaningfully larger than for most enterprise AI applications. A single large 3D seismic survey run through a full ML processing pipeline (noise suppression, multiple attenuation, fault detection, horizon picking) can require hundreds to thousands of GPU-hours. At scale across a multi-basin portfolio, this represents a non-trivial compute footprint.

The environmental cost has two components:

- **Direct compute energy.** Cloud GPU instance costs serve as a proxy; the underlying energy consumption maps to carbon cost via the grid carbon intensity of the cloud region used. IEA *Energy and AI* (2025) projects data-centre demand growing to ~945 TWh by 2030; operator-level compute is a fraction of this aggregate but is growing with adoption.
- **Disclosure and compliance overhead.** E&P companies under TCFD, SEC climate rules, or EU CSRD are required to report Scope 3 emissions from their supply chains. Cloud AI compute falls within this scope and requires measurement, reporting, and audit infrastructure.

**Range (annual, ongoing):** $25k–$100k/year — primarily cloud compute energy cost and growing disclosure overhead. *Assumption: Based on Luccioni, Jernite & Strubell (2024) per-inference energy coefficient applied to a GPU-intensive seismic ML workload `[VERIFY: apply to specific GPU-hour volumes for representative survey sizes]`. Carbon cost modelled at $30–$150 / tonne CO₂e as shadow pricing `[VERIFY with applicable carbon pricing regime]`.*

### Category 6: Labour & Supply Chain  *(Sector lens: Medium)*

Training data for seismic AI models requires geological facies labelling and horizon picks annotated by geoscientists — not general-purpose data annotators. This creates a specialist and relatively expensive annotation market with limited scalability. Two cost components:

- **Training data annotation.** Initial model training requires labelled seismic examples from geoscientists with domain expertise. This is typically contracted to specialist geoscience service companies or performed internally by senior staff, competing with live interpretation time. `[VERIFY with annotation contractor pricing in seismic domain]`
- **Data sovereignty compliance.** Seismic data is government-regulated in most producing nations. In Norway, the NPD (Sokkeldirektoratet) requires that seismic data over the Norwegian Continental Shelf be registered and, for certain licensed data, restricted from export without approval. Similar frameworks exist in Brazil (ANP), the UK (NSTA), Nigeria (NUPRC), and other producing jurisdictions. Transferring seismic datasets to a cloud AI platform's training or inference environment may require legal review and, in some cases, government notification or approval. This is a real compliance overhead that is absent from vendor procurement timelines. `[VERIFY: current data sovereignty requirements by jurisdiction for cloud-based seismic processing]`

**Range (one-off + ongoing):** $30k–$150k total — annotation, contractor cost, and sovereignty compliance overhead. *Illustrative assumption; varies substantially with jurisdiction and portfolio composition.*

### Category 7: Governance & Shadow AI  *(Sector lens: High)*

The governance costs in this use case are elevated by three factors unique to subsurface AI:

**Reserves audit trail.** As described in Category 3, AI-assisted reserves estimates require an auditable methodology. The governance cost of establishing and maintaining this documentation regime — model versioning policy, training data retention, interpretive decision logs — is an ongoing overhead that does not diminish after the initial deployment.

**Seismic data sovereignty (detailed).** Beyond the annotation pipeline described in Category 6, the production use of AI interpretation on sovereign resource data creates ongoing governance obligations: tracking which data has been shared with which cloud or vendor environment, managing data residency commitments under cloud contracts, and ensuring that vendor agreements explicitly address intellectual property in AI models trained on sovereign seismic data. In a PSC (Production Sharing Contract) environment, the host government may claim ownership of insights derived from seismic data on which it holds a regulatory interest.

**Model governance for high-stakes decisions.** A seismic AI model whose output informs a drilling decision worth $20M–$500M is a materially different governance object than a content-moderation classifier or a product recommendation engine. Model risk management principles — analogous to those mandated in financial services (SR 11-7) but not yet regulated in E&P — are nonetheless warranted here given the financial stakes. Who approves a model version for use on a live drilling-decision workflow? What triggers revalidation? Who bears liability if a model failure leads to a dry hole?

**Range (annual, ongoing):** $50k–$200k/year — legal and governance overhead for data sovereignty compliance, model IP clauses, reserves-audit documentation, and ongoing model risk management. *Illustrative assumption; highly context-specific. JV and PSC structures add to this cost. `[VERIFY with O&G AI governance cost studies]`*

---

## 3. Full Valuation Outputs

### TCO summary (Year 1, illustrative ranges)

<div style="position:relative;max-width:760px;margin:1.5rem auto;">
  <canvas id="subsurface-tco-chart" aria-label="Horizontal grouped bar chart: illustrative Year-1 cost range by category (low and high estimates in US$000s)"></canvas>
</div>
<script>
(function () {
  var el = document.getElementById('subsurface-tco-chart');
  if (!el || typeof Chart === 'undefined') return;
  new Chart(el, {
    type: 'bar',
    data: {
      labels: [
        'Visible spend (Year 1)',
        'Technical & op debt (annual)',
        'Integration overrun risk',
        'Verification overhead (annual)',
        'Cognitive discount (on benefits)',
        'Environmental (annual)',
        'Labour & supply chain',
        'Governance overhead (annual)'
      ],
      datasets: [
        {
          label: 'Low estimate (US$000s)',
          data: [730, 40, 60, 80, 35, 25, 30, 50],
          backgroundColor: 'rgba(63,81,181,0.80)',
          borderColor: 'rgba(63,81,181,1)',
          borderWidth: 1,
          borderRadius: 3
        },
        {
          label: 'High estimate (US$000s)',
          data: [2300, 200, 420, 300, 200, 100, 150, 200],
          backgroundColor: 'rgba(255,152,0,0.70)',
          borderColor: 'rgba(255,152,0,1)',
          borderWidth: 1,
          borderRadius: 3
        }
      ]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Illustrative Year-1 Cost Range by Category (US$000s)',
          font: { size: 13, weight: 'bold' }
        },
        subtitle: {
          display: true,
          text: 'All figures illustrative — see text for assumptions and [VERIFY] markers',
          font: { size: 10 },
          color: '#888'
        }
      },
      scales: {
        x: {
          beginAtZero: true,
          title: { display: true, text: 'US$000s (illustrative)' }
        }
      }
    }
  });
}());
</script>

### Low / Base / High scenarios

| Scenario | Visible (Year 1) | Hidden (Year 1) | **Full TCO Year 1** | Hidden as % of visible |
|---|---|---|---|---|
| Low | $730k | $320k | **$1,050k** | ~44% |
| Base | $1,400k | $730k | **$2,130k** | ~52% |
| High | $2,300k | $1,370k | **$3,670k** | ~60% |

*All figures illustrative. The hidden cost share is structurally higher here than in operationally-focused AI deployments because reserves-audit and governance overhead is relatively fixed regardless of platform scale.*

### Key sensitivities

The three assumptions that move the result most:

1. **Seismic data sovereignty jurisdiction.** An operator with a portfolio concentrated in jurisdictions with stringent data-residency requirements (Norway, Brazil, certain MENA states) faces significantly higher legal and compliance overhead than one operating in less-regulated environments. This is binary rather than continuous — a single jurisdictional constraint can halt a cloud-based deployment entirely and require an on-premise or hybrid architecture, adding $200k–$600k to integration cost. `[VERIFY with current regulatory positions in target jurisdictions]`

2. **Reserves reporting scope.** If AI-interpreted surveys underpin SEC-reportable proved reserves, verification and governance overhead is at the upper end of its range. If AI is used only for prospect ranking and no AI-derived interpretation directly enters a reserves estimate, the reserves-audit burden is much lower. This is often not decided at the procurement stage — it depends on how the AI is actually used after deployment.

3. **Platform portability vs. vendor lock-in.** The total cost difference between an open, well-documented AI platform (one where the operator can retrain models internally) and a closed black-box SaaS platform is large over a 5-year horizon. The open platform has higher Year-1 integration costs and requires internal ML capability; the closed SaaS has lower Year-1 costs but accumulates vendor-dependency debt that is expensive to reverse.

!!! warning "No single NPV figure is presented here"
    The scenario table above shows a TCO range. Converting this to an NPV would require benefit assumptions — dry-hole reduction rates, FID acceleration value, storage-capacity certification savings — that are highly site-specific, geologically dependent, and at this stage largely unverified by the operator's own data. The most commonly cited AI seismic benefits (50–80% cycle-time reduction, dry-hole rates halved) come from vendor marketing and should not be used as unverified benefit inputs to a business case. Presenting a single NPV at this stage would be an analysis placebo. See [Measurement Discipline](../methodology/measurement-discipline.md).

---

## 4. Key Uncertainties & Governance

### Value-of-information framing

Before committing to a multi-basin enterprise licence, the measurements most likely to narrow the TCO uncertainty are:

| Question | Why it matters | Suggested measurement |
|---|---|---|
| Which jurisdictions in the portfolio have data-residency requirements for seismic data? | Binary: a single hard constraint changes the architecture from cloud to hybrid/on-premise, adding $200k–$600k | Legal review of data licence terms and host-country regulations before signing any cloud AI contract |
| Will AI-derived interpretations underpin SEC-reportable proved reserves? | Determines whether reserves-audit overhead is at Low (~$80k/yr) or High (~$300k/yr) | Internal reserves reporting review before deployment scope is finalised |
| What is the baseline interpretation throughput and dry-hole rate against which AI improvement will be measured? | Without a pre-AI baseline, benefit measurement is impossible — the vendor's claimed improvement cannot be verified | Instrument interpretation workflows during POC: log time per interpretation decision, log prospect outcomes over 12–24 months |
| What is the model's out-of-basin generalisation performance? | Drives technical-debt severity — poor generalisation means per-basin retraining cost | Run the POC model on a held-out dataset from a geologically distinct basin before committing to multi-basin rollout |

Spending $40k–$100k on these four measurements before committing to a multi-million-dollar enterprise licence is defensible on value-of-information grounds: each measurement resolves a cost uncertainty that individually spans $200k–$500k over a five-year horizon.

### Governance: the reserves audit trail

The reserves-booking governance dimension has no analogue in other AI use cases and deserves extended treatment.

**What the "reliable technology" standard requires.** Under SEC Rules 4-10(a)(22), a technology is "reliable" for proved-reserves booking if it has been field-tested, has demonstrated production results or has a sound theoretical basis, and is capable of making a meaningful distinction between proved and unproved resources. AI seismic interpretation platforms are not automatically compliant with this standard. Compliance requires: (a) documentation that the model has been validated against drilled outcomes; (b) a mechanism for the QRE to understand the basis for the model's picks; and (c) version control that allows a specific estimate to be attributed to a specific model version.

**The explainability problem.** Many commercial seismic AI systems use deep-learning architectures — CNNs, U-Nets, transformers — whose internal workings are not directly interpretable. A QRE asked to certify reserves based on a U-Net horizon pick cannot, in general, explain why the model placed the pick at a particular location. Satisfying the audit standard requires either additional explainability tooling (attention maps, integrated gradients, sensitivity analysis) or a validation framework that substitutes statistical back-testing for mechanistic explanation.

**Practical implication.** The governance cost of reserves-audit compliance is a one-off architecture investment ($100k–$250k to build the documentation and validation framework) plus an ongoing per-estimate overhead ($30k–$80k per audited reserves report involving AI-derived interpretations). These are additional to the Category 7 annual range above and should be modelled separately for operators with material SEC-reportable reserves. `[VERIFY with QRE and reserves auditor guidance on AI methodology compliance]`

### Governance: two contrasting regulatory environments

These two profiles illustrate how the governance environment reshapes the indirect-cost distribution. They are illustrative, not benchmarks.

**Norwegian Continental Shelf (NCS).** The Norwegian offshore data environment is among the most tightly regulated in the world. Seismic data acquired on the NCS is subject to registration with the Sokkeldirektoratet (previously the Norwegian Petroleum Directorate); certain data categories require government approval before being shared with third-party cloud environments. PSA (Petroleum Safety Authority) requirements for computational systems used in safety-adjacent contexts add further governance overhead. Operators active on the NCS who deploy cloud-based AI seismic interpretation must ensure that their cloud contracts and data architectures are consistent with these requirements before processing. The Northern Lights CCS project (Equinor, TotalEnergies, Shell) illustrates the CCUS qualification sub-scenario: subsurface AI tools are being applied to characterise the Johansen and Cook Formations for CO₂ injection — a use case where the verification and governance overhead is further elevated by permitting requirements. `[VERIFY: current NPD/Sokkeldirektoratet requirements for cloud-based seismic data processing; Northern Lights AI methodology documentation]`

**UAE (Abu Dhabi).** ADNOC has publicly invested in AI across its upstream operations and has an active AI Centre of Excellence. The regulatory environment for seismic data in Abu Dhabi is governed by the Supreme Council for Energy and ADNOC's own data governance framework. The computational governance context differs materially from the NCS: data-residency requirements are evolving, and the UAE's National AI Strategy creates a different incentive landscape for cloud-based AI adoption. For operators working in a CCUS or EOR (Enhanced Oil Recovery) context in Abu Dhabi, the governance footprint is shaped by ADNOC's internal model validation requirements and any applicable Abu Dhabi Global Market (ADGM) or TDRA AI frameworks. `[VERIFY: current ADNOC and UAE regulatory requirements for AI seismic processing and CCUS characterisation]`

The key point from this comparison is not which environment is "better" but that the governance overhead is environment-specific and must be assessed before deployment architecture is committed. An operator active in both NCS and UAE cannot apply a single governance model to its seismic AI deployment.

---

## 5. Recommendation

!!! quote "Decision-quality statement (not a verdict)"
    **Resolve jurisdictional constraints and reserves-reporting scope before signing an enterprise licence.**

    The illustrative TCO range ($1.0M–$3.7M in Year 1) is wide enough that proceeding without resolving the three binary uncertainties — data-residency jurisdictions, reserves-reporting scope, and model portability — exposes the operator to cost overruns that could triple the visible spend.

    The conditional recommendation is:

    **Proceed to enterprise rollout if:** (a) legal review confirms that all portfolio jurisdictions allow cloud-based seismic processing under the proposed architecture; (b) the operator's reserves-reporting team confirms that AI-derived interpretations will not underpin SEC-reportable proved reserves in Year 1–2 without a validation framework in place; and (c) the POC model demonstrates out-of-basin generalisation performance above a pre-agreed QC threshold.

    **Stage the rollout if:** data-residency constraints require a hybrid architecture for some jurisdictions but not others. Apply the platform in compliant jurisdictions first, use that deployment to build the validation and audit-trail infrastructure, and extend to constrained jurisdictions once the governance framework is in place.

    **Defer enterprise commitment if:** the reserves-reporting team confirms that AI-picked prospects will flow directly to proved-reserves estimates in Year 1, before a validation framework exists. The cost of a premature reserves certification failure — regulatory investigation, reserves restatement, investor litigation — far exceeds the cost of a six-month delay to establish compliant QC infrastructure.

    The value of AI seismic interpretation is real: the research literature from geoscience AI groups (NR.no and others) documents genuine cycle-time reductions in horizon picking and fault detection. The question for this operator is not whether the technology works — it is whether *this organisation, with this portfolio, in these jurisdictions, reporting to these stakeholders* can deploy it in a way that the governance and verification infrastructure actually supports.

---

## Evidence references

| Claim | Source |
|---|---|
| 2–3× cost expansion; 40–60% hidden cost share | Anyreach (2026) — [Bibliography](../evidence/bibliography.md) |
| Fat-tailed IT project overrun distribution | Flyvbjerg & Budzier (2011), *HBR* — [Bibliography](../evidence/bibliography.md) |
| ML technical debt accumulation; CACE principle | Sculley et al. (2015), NeurIPS 28 — [Bibliography](../evidence/bibliography.md) |
| Cognitive offloading and AI tool use | Gerlich (2025) — [Bibliography](../evidence/bibliography.md) |
| Analysis placebo / measurement discipline | Hubbard, D. W. — [Measurement Discipline](../methodology/measurement-discipline.md) |
| AI seismic interpretation research | NR.no Subsurface AI Group — directional reference `[VERIFY full citation]` |
| SEC "reliable technology" standard | US SEC Rules 4-10(a)(22) `[VERIFY current guidance]` |
| SPE-PRMS reserves classification guidelines | SPE (2018) *Petroleum Resources Management System* `[VERIFY edition]` |
| GPU-hour energy coefficient for ML workloads | Luccioni, Jernite & Strubell (2024), FAccT '24 — [Literature](../literature/bibliography.md) |
| Data-centre demand trajectory | IEA *Energy and AI* (2025) — [Literature](../literature/bibliography.md) |
| Northern Lights CCUS project (illustrative) | Equinor public disclosures `[VERIFY AI methodology citations]` |
| Energy sector AI initiative failure rate | AI in Energy Summit 2026 — [Energy: Pilot Gap](../evidence/energy-pilot-gap.md) |
