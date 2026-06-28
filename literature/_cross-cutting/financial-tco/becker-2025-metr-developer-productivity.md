---
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
authors: "Becker, Joel; Rush, Nate; Barnes, Beth; Rein, David"
year: 2025
type: working-paper
publisher: "METR (Model Evaluation & Threat Research)"
identifier: "arXiv:2507.09089 · https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
primary_sector: cross-sector
sectors: [11-technology-software-telecom, 14-human-capital-hr-future-of-work]
value_dimensions: [productivity, time-returned]
cost_dimensions: [time, trust-accountability, cognitive-skills]
stance: reality-check
flags: [INDEPENDENT, RCT, EARLY-2025-TOOLS-SNAPSHOT]
key_metrics: "AI-allowed tasks 19% slower (95% CI +2% to +39%); devs forecast 24% speedup, believed 20% speedup post-hoc; experts forecast ~38–39% speedup; n=16 devs, 246 tasks, early-2025 tools (Cursor Pro + Claude 3.5/3.7)"
relevance_to_valorai: "Independent, non-vendor RCT anchor for the perceived-vs-actual productivity gap; the empirical core of the analysis-placebo problem. Triangulates self-reported time-savings (e.g., Glean Work AI Index 11 hrs/wk) and sets a ceiling on expected developer-context gains."
---

## Summary

Randomised controlled trial: 16 experienced open-source developers completed 246 real tasks
in mature repositories they knew well (~5 yrs experience, large high-standard codebases), each
task randomly assigned AI-allowed or AI-disallowed (Cursor Pro + Claude 3.5/3.7 Sonnet). AI-
allowed tasks took 19% longer (95% CI: +2% to +39%). The perception gap was large: developers
forecast a 24% speedup and, even after experiencing the slowdown, still estimated a 20% gain;
economics and ML experts had forecast ~38–39%. The authors tested 21 possible confounds and
found the slowdown robust.

## What it lets valorai measure

The independent counterweight to self-reported time-savings figures. It quantifies the distance
between *felt* and *actual* productivity in a controlled, non-vendor setting — the exact
measurement failure ValorAI exists to correct. Primary use: the triangulation anchor for any
verification- or productivity-category estimate sourced from self-report.

## Caveats / limits

High internal validity (RCT); limited external validity. Experienced devs on large, mature,
high-quality-bar codebases they know intimately — likely the hardest setting for AI to help;
results may not transfer to greenfield work, unfamiliar code, or junior developers. Early-2025
model snapshot (Cursor Pro + Claude 3.5/3.7 Sonnet), since superseded. Small n (16 devs).
METR's Feb-2026 follow-up on late-2025 tools became unreliable because developers increasingly
refused to work without AI (selection-bias attrition), so treat 19% as an early-2025 *snapshot*,
not a fixed constant. Do not extrapolate to non-developer knowledge-work.

## Citation

Becker, J., Rush, N., Barnes, B. & Rein, D. (2025). *Measuring the Impact of Early-2025 AI on
Experienced Open-Source Developer Productivity.* METR. arXiv:2507.09089.
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
