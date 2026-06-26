# Valuation Models

## The Standard Identity — and Its Failure Mode

The conventional formula for AI return on investment is:

```
ROI = (Tangible Benefits + Intangible Benefits − Total Cost of Ownership) / TCO
```

Computed over a 12–24 month horizon, with payback period, net present value (NPV), and internal rate of return (IRR) as supplementary metrics, this identity is mathematically sound. The failure is not in the formula — it is in what organisations put into it.

When TCO is defined as subscription fees plus a one-time implementation estimate, the formula produces a large positive number. When TCO is defined as the full lifecycle cost of owning and operating an AI system — including the seven categories of indirect cost documented in this framework — the formula frequently produces a much more modest result, and sometimes a negative one. The difference is not a matter of pessimism. It is a matter of completeness.

A naive ROI calculation that omits indirect costs is precisely the **analysis placebo** described in [Measurement Discipline](measurement-discipline.md): it feels rigorous, it generates a confident number, and it does not accurately represent the decision.

---

## Full-Lifecycle Total Cost of Ownership

A defensible AI TCO model must treat the following as explicit line items, not residuals.

### Visible Costs (Tier 1)

| Item | Notes |
|---|---|
| Licence / API fees | Subscription, per-seat, or consumption-based pricing |
| Compute infrastructure | Cloud GPU/TPU spend, inference costs at scale |
| Initial implementation | Integration engineering, configuration, data preparation |
| Training and change management | Staff upskilling, process redesign |

### Indirect Costs (Tier 2 — typically 40–60% of total project cost)

| Category | Representative Cost Drivers |
|---|---|
| Technical & operational debt | Model retraining, pipeline maintenance, drift monitoring, dependency updates |
| Integration & implementation overrun | Hidden integration work beyond initial scope; 2–3× cost expansion is the base-rate expectation |
| Verification & oversight | Human review hours required to validate AI outputs before use |
| Cognitive & human-capital erosion | Deskilling, automation-bias incidents, knowledge-management overhead |
| Environmental externalities | Energy and water costs; carbon pricing or offset obligations; disclosure compliance |
| Labour & supply-chain | Annotation and moderation contractor costs; ESG audit and remediation exposure |
| Governance & shadow AI | Unmanaged AI tool usage carrying data-leakage and compliance risk; tooling and audit costs |

The 40–60% figure is drawn from independent research aggregated in the [Base Rates table](../evidence/base-rates.md). It is a finding about *existing practice*, not a pessimistic assumption — organisations that plan for these costs explicitly tend to experience smaller overruns.

### Structuring the TCO Calculation

For a 24-month horizon:

```
TCO = Σ (Tier 1 costs)_t + Σ (Tier 2 costs)_t    for t = 1..24 months

NPV of benefits = Σ [ (Tangible_t + Intangible_t) / (1 + r)^t ]

NPV of investment = Σ [ TCO_t / (1 + r)^t ]

Net NPV = NPV of benefits − NPV of investment

IRR = discount rate at which Net NPV = 0

Payback period = month t* at which cumulative benefits first exceed cumulative TCO
```

Where `r` is the organisational hurdle rate or weighted average cost of capital. Intangible benefits (risk reduction, option value, brand) should be estimated using structured decomposition rather than left as qualitative statements — see the value-of-information section below.

---

## Real Options

Many AI investments are better analysed as option portfolios than as committed capital expenditures. A pilot deployment is not merely a small version of a full rollout — it is an *option to expand*, whose value includes the information it generates about whether full deployment is warranted.

Treating pilots as options has several practical consequences:

- The cost of a pilot that is subsequently abandoned is not a sunk cost — it is the premium paid for information that prevented a larger mistake.
- The decision to *not* pilot (and instead commit directly to full deployment) implicitly forgoes this option, which has a calculable value.
- The optimal time to exercise the option (proceed to full deployment) depends on how much uncertainty is resolved by the pilot and how quickly the competitive environment evolves.

A simple real-options framing uses the Black-Scholes model or a binomial lattice, treating the present value of the full deployment as the underlying asset, deployment cost as the strike price, time to decision as the option duration, and forecast uncertainty as the volatility parameter. Practitioners without options-pricing expertise can approximate the same reasoning by asking: *given what the pilot has revealed, what is the probability that full deployment produces positive NPV?* That probability, multiplied by the expected NPV if positive, minus the option premium already paid, is the adjusted option value.

---

## Value of Information

Hubbard's framework introduces a powerful decision criterion: before commissioning additional analysis, compute the **expected value of perfect information (EVPI)** for the key uncertain variables in the model.

The procedure:

1. Identify the uncertain variable with the highest impact on the NPV calculation (often integration cost or adoption rate).
2. Estimate the range of outcomes if that variable is at the pessimistic end versus the optimistic end.
3. Compute the decision difference: if the pessimistic value makes the investment NPV-negative, and you would not proceed under that scenario, the value of knowing the true value is bounded by the cost of the mistake you would avoid.
4. Compare that value to the cost of obtaining better information (a more detailed technical assessment, a scoping engagement with the integration partner, a structured survey of end-user adoption intent).
5. Commission additional analysis only if the expected value of information exceeds its cost.

This procedure prevents two common failure modes: under-investing in diligence (proceeding without understanding a key driver) and over-investing in diligence (conducting exhaustive analysis on variables that do not change the decision).

---

## Worked Caution: The Analysis Placebo in Practice

Consider a standard AI procurement business case:

- Vendor claims 30% productivity improvement for a team of 50 analysts at £60k average salary
- Projected benefit: 0.30 × 50 × £60,000 = **£900k per year**
- Subscription cost: £120k per year
- Implementation (vendor estimate): £80k one-time
- Headline ROI: (£900k − £200k) / £200k = **350%**

Now apply the full TCO model with even conservative indirect-cost estimates:

- Integration overrun (50% of visible costs, well below the 2–3× base-rate expectation): +£100k
- Verification overhead (15% of analyst time spent validating outputs): −£135k benefit reduction
- Ongoing model maintenance and retraining: +£40k/year
- Governance and shadow-AI audit tooling: +£20k/year
- Deskilling provision and knowledge management: +£30k/year

Revised first-year cost: £390k. Revised benefit: £765k. Revised ROI: 96%. Year-two and beyond requires retraining, further integration work, and growing oversight overhead — the payback trajectory is fundamentally different.

The original 350% figure is not fraudulent. Every number in it is defensible in isolation. The problem is structural omission. The analysis placebo does not fabricate results — it simply does not ask the full question.

---

## References

- Hubbard, D. W., Budzier, A. & Bang Leed, A. *How to Measure Anything in Project Management.* Wiley.
- Anyreach (2026). *The Hidden Costs of AI in Business.* — 2–3× cost expansion; 40–60% hidden cost share.
- Meta-Intelligence (2025). *State of AI in Business.* — 13% quantifiable-value base rate.
- MIT NANDA (2025). *The GenAI Divide: State of AI in Business 2025.* — 95% no-P&L base rate.
