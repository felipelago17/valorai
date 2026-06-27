---
title: "Power Hungry Processing: Watts Driving the Cost of AI Deployment?"
authors: "Luccioni, A. S., Jernite, Y. & Strubell, E."
year: 2024
type: conference-paper
publisher: "ACM FAccT 2024"
identifier: "DOI: 10.1145/3630106.3658542; arXiv:2311.16863"
primary_sector: cross-sector
sectors: [cross-sector]
value_dimensions: []
cost_dimensions: [environmental]
stance: cost-cautionary
key_metrics:
  - "Generative and multipurpose models substantially more energy-intensive per query than task-specific models"
  - "Per-inference energy consumption measured empirically across a range of model families"
  - "Carbon emissions per inference calculable from energy × grid carbon intensity"
relevance_to_valorai: Provides per-use environmental cost coefficients by model type; enables energy and carbon cost calculation as a function of query volume in the TCO ledger.
---

## Summary

Luccioni, Jernite and Strubell measured the energy consumption of a range of AI model families at inference time, comparing generative large language models against smaller task-specific models. Generative models are substantially more energy-intensive per inference than task-specific alternatives, which has direct implications for the environmental cost of choosing a general-purpose versus specialised AI tool. The work provides empirical coefficients suitable for insertion into environmental cost calculations. Preprint circulated November 2023 (arXiv:2311.16863); published in FAccT 2024 proceedings.

## What it lets valorai measure

Enables per-query environmental cost scoring: multiply query volume by per-inference energy coefficient, convert to carbon using grid intensity, and include in TCO ledger alongside financial costs.

## Caveats / limits

Energy coefficients depend on hardware and batching configuration; apply with awareness of deployment-specific variation. Note: the filename retains the preprint year (2023) but the canonical citation year is 2024 (proceedings).

## Citation

Luccioni, A. S., Jernite, Y. & Strubell, E. (2023). Power hungry processing: Watts driving the cost of AI deployment? In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24),* pp. 85–99. https://doi.org/10.1145/3630106.3658542. Preprint: arXiv:2311.16863.
