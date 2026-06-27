# Cross-Cutting Lens: Environmental

This lens captures the physical resource costs of AI systems — energy consumption, freshwater use, carbon emissions, land occupied by data-centre infrastructure, and e-waste generated at end of hardware life. These costs were historically treated as externalities but are increasingly internalised through carbon pricing, water-risk frameworks, mandatory climate disclosure (e.g. CSRD, SEC climate rules), and ESG investor scrutiny.

**Scoring across sectors:** Apply per-inference energy and water coefficients (sourced from Luccioni et al. and Li et al.) to estimated workload volumes. Weight by local grid carbon intensity and water-stress level. Add hardware embodied-carbon and end-of-life disposal for capital-intensive AI infrastructure. Flag regulatory exposure where applicable.

## Sources filed here

- `luccioni-2023-power-hungry-processing.md` — per-inference energy cost by model type `[VERIFY]`
- `li-2023-ai-less-thirsty.md` — freshwater footprint of training and inference
