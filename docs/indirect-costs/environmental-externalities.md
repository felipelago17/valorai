# Environmental Externalities

## Definition

AI systems are material systems. Their operation requires physical infrastructure — data centres, networking equipment, cooling apparatus, end-user devices — with substantial resource demands: electricity, water, land, and the rare materials embedded in hardware. The environmental costs of this infrastructure have historically been treated as externalities: costs borne by ecosystems and communities rather than appearing on an AI project's balance sheet.

This is changing. Carbon pricing mechanisms, water-risk frameworks, mandatory climate disclosure regulations, and growing investor scrutiny are converting what were previously unpriced externalities into real financial liabilities. An AI valuation that does not account for environmental costs is not merely incomplete — it is likely to be revised as these costs are progressively internalised.

## The Evidence

### Carbon Footprint

Estimates of AI's aggregate carbon footprint carry wide uncertainty bands, reflecting the diversity of hardware configurations, energy sources, and estimation methodologies in use. Research aggregated by ScienceDirect (2025) places AI's total carbon footprint at approximately **32.6–79.7 million tonnes of CO₂ equivalent** for 2025. This range spans a factor of roughly 2.5, reflecting genuine uncertainty rather than methodological sloppiness — the lower bound reflects optimistic assumptions about grid decarbonisation and hardware efficiency, while the upper bound applies more conservative assumptions.

For individual organisations, the relevant question is not the aggregate but the attributable share: what portion of this footprint corresponds to the AI systems the organisation operates or procures? This calculation requires knowing the energy consumption of the relevant compute, the carbon intensity of the electricity grid supplying that compute, and the embodied carbon of the hardware involved.

### Water Footprint

Data centre cooling requires substantial quantities of water. Li and colleagues (2023) documented what they termed the "secret water footprint" of AI models, drawing attention to the gap between the public discussion of AI's energy use and the largely unreported water consumption associated with cooling. A useful approximation is that data centre cooling systems consume approximately **2 litres of water per kilowatt-hour of electrical energy consumed** (MIT News 2025), though this varies significantly by cooling technology, climate zone, and local infrastructure.

At aggregate scale, ScienceDirect (2025) estimates AI's total water footprint for 2025 at approximately **312.5–764.6 billion litres** — a range carrying the same uncertainty structure as the carbon estimates. The lower bound assumes widespread adoption of more efficient cooling technologies; the upper bound applies current average consumption rates.

The financial materiality of water consumption is highest in water-stressed regions, where operational risk from water scarcity, water pricing, or regulatory restrictions on consumption can directly affect data centre operations.

### Material and Land Footprint

The UN University INWEH (2025) frames AI's environmental cost as a material-system issue, not merely an energy one. Hardware production requires rare earth elements and other critical minerals mined under conditions that carry both environmental and social costs. Data centres occupy land, often in areas with competing uses. End-of-life hardware generates e-waste that is disproportionately managed in low-income countries under conditions that transfer health and environmental risks to those communities.

### The Environmental Justice Dimension

UNU INWEH (2025) explicitly positions AI's environmental costs within an environmental justice framework: the harms are borne disproportionately by communities that are not the primary beneficiaries of AI's productivity gains. This framing is increasingly reflected in regulatory and litigation environments, creating legal and reputational exposure for organisations whose AI supply chains are concentrated in vulnerable regions.

## How This Enters the Valuation

Environmental externalities should appear in the TCO model as:

- **Carbon cost** — energy consumption estimate × carbon intensity of supply × applicable carbon price (or shadow carbon price if no explicit pricing applies). As carbon pricing extends geographically and sectorally, organisations that do not price carbon internally are deferring a real cost.
- **Water cost and risk** — water consumption estimate × local water price, with a risk premium for data centre locations in water-stressed regions.
- **Disclosure and compliance overhead** — the cost of measuring, reporting, and auditing environmental performance under applicable disclosure requirements (CSRD in the EU, SEC climate disclosure in the US, TCFD-aligned frameworks globally).
- **Stranded asset risk** — hardware and data centre investments in jurisdictions likely to face more stringent environmental regulation may carry higher effective cost than their purchase price suggests.

Environmental cost estimates carry inherent uncertainty and should be presented as ranges rather than point estimates. The wide uncertainty in published aggregate figures reflects genuine measurement challenges, not unreliability of the underlying phenomenon.

---

## References

- United Nations University INWEH (2025). *Environmental Cost of Artificial Intelligence: Carbon, Water and Land Footprints of AI Systems.* — Material-system framing; environmental justice; aggregate footprint estimates.
- Li, P., Yang, J., Islam, M. A. & Ren, S. (2023). *Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models.* arXiv:2304.03271.
- Nature Sustainability (2025). *Environmental impact and net-zero pathways for sustainable AI servers in the USA.* — US-focused water and carbon footprint projections.
- MIT News (2025). *Water consumption of AI and data centres.* — 2 L/kWh cooling approximation. `[VERIFY]`
- ScienceDirect (2025). Aggregate AI carbon and water footprint estimates, 32.6–79.7 Mt CO₂ and 312.5–764.6 bn L. — `[VERIFY specific article citation]`
