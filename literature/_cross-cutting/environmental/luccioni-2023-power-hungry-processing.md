---
title: "Power Hungry Processing: Watts Driving the Cost of AI Deployment?" [VERIFY exact title]
authors: "Luccioni, A. S., Jernite, Y. & Strubell, E. [VERIFY full author list]"
year: 2023
type: working-paper
publisher: "[VERIFY venue — FAccT 2024 or arXiv]"
identifier: "[VERIFY DOI or arXiv ID]"
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

Luccioni and colleagues measured the energy consumption of a range of AI model families at inference time, comparing generative large language models against smaller task-specific models. Generative models are substantially more energy-intensive per inference than task-specific alternatives, which has direct implications for the environmental cost of choosing a general-purpose versus specialised AI tool. The work provides empirical coefficients suitable for insertion into environmental cost calculations.

## What it lets valorai measure

Enables per-query environmental cost scoring: multiply query volume by per-inference energy coefficient, convert to carbon using grid intensity, and include in TCO ledger alongside financial costs.

## Caveats / limits

`[VERIFY]` Exact title, full author list, and publication venue require confirmation before citing in published material. Energy coefficients depend on hardware and batching configuration; apply with awareness of deployment-specific variation.

## Citation

Luccioni, A. S. et al. (2023). *[VERIFY title].* `[VERIFY venue and DOI]`.
