"""
Seismic Interpretation AI Workflow — Proof-of-Concept Pipeline
==============================================================

Purpose
-------
This file illustrates the computational structure of an AI-assisted seismic
interpretation pipeline. It is intended as an educational reference for
geoscientists and data engineers evaluating ML seismic platforms. It is NOT
production code: it uses pseudocode stubs where a real implementation would
require proprietary libraries, calibrated model weights, or survey-specific
configuration.

Companion document:
    docs/use-cases/oil-gas-subsurface-ai.md
KPI model:
    docs/metrics/subsurface-ai-kpis.json

Key computational steps:
    1. SEG-Y data ingestion and format normalisation
    2. Seismic preprocessing (amplitude normalisation, bandpass filtering)
    3. Deep-learning horizon picking (U-Net family)
    4. Fault detection (3D CNN)
    5. Seismic facies classification (self-supervised + supervised)
    6. Uncertainty quantification (Monte Carlo dropout ensemble)
    7. Output — horizon/fault picks in standard exchange formats

Dependencies (production implementation would require):
    segyio           >= 1.9          SEG-Y I/O
    numpy            >= 1.24
    scipy            >= 1.11
    torch            >= 2.0          or tensorflow >= 2.13
    segysak          >= 0.5          (optional) higher-level SEG-Y handling
    xtgeo            >= 3.0          Petrel-compatible surface I/O

All cost and performance figures in comments are illustrative ranges.
Mark [VERIFY] where production experience data would be needed.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
import scipy.signal as signal

# segyio is the standard SEG-Y I/O library for Python.
# In a production environment, install with: pip install segyio
try:
    import segyio
    SEGYIO_AVAILABLE = True
except ImportError:
    SEGYIO_AVAILABLE = False
    logging.warning("segyio not installed — SEG-Y loading will use stub. pip install segyio")

# PyTorch for deep-learning inference. TensorFlow can substitute.
try:
    import torch
    import torch.nn as nn
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    logging.warning("torch not installed — inference will use stub. pip install torch")

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class SeismicSurvey:
    """Minimal representation of a loaded 3D seismic cube."""
    data: np.ndarray          # shape: (n_inlines, n_crosslines, n_samples)
    sample_rate_ms: float     # ms per sample (typically 1–4 ms)
    inline_start: int
    crossline_start: int
    cdp_x: Optional[np.ndarray] = None   # shape: (n_inlines, n_crosslines)
    cdp_y: Optional[np.ndarray] = None
    segy_path: Optional[Path] = None

    @property
    def shape(self) -> tuple[int, int, int]:
        return self.data.shape  # type: ignore[return-value]


@dataclass
class InterpretedHorizon:
    """A single picked horizon as a 2D time/depth surface."""
    name: str
    twt_ms: np.ndarray           # shape: (n_inlines, n_crosslines), two-way time in ms
    confidence: np.ndarray       # shape: same; values [0, 1]
    uncertainty_ms: np.ndarray   # shape: same; 1-sigma uncertainty in ms
    provenance: str = "ai-mc-dropout"  # epistemic provenance tag


@dataclass
class FaultProbabilityVolume:
    """Voxel-wise fault probability from 3D CNN."""
    probability: np.ndarray    # shape: (n_inlines, n_crosslines, n_samples); [0, 1]
    threshold: float = 0.5     # probability threshold for binary fault/no-fault
    provenance: str = "ai-cnn"


# ---------------------------------------------------------------------------
# Step 1: SEG-Y ingestion
# ---------------------------------------------------------------------------

def load_segy(segy_path: Path, byte_locs: Optional[dict] = None) -> SeismicSurvey:
    """
    Load a 3D seismic volume from SEG-Y.

    byte_locs: optional dict specifying non-standard header byte locations,
        e.g. {"inline": 189, "crossline": 193} (these are the SEG-Y Rev1 defaults).

    Governance note: Before loading, confirm the data licence permits cloud
    or off-premises processing. In some jurisdictions (NCS, Brazil ANP)
    this requires operator confirmation. See use-case governance section.

    Compute cost note: A 500 km² 3D survey at 6.25 m bin spacing and 4 ms
    sample rate occupies ~2–8 GB in SEG-Y. Loading to memory is fast;
    full-volume ML inference requires GPU-resident data and scales with
    volume size. [VERIFY: GPU-hour estimates for representative volumes]
    """
    if not SEGYIO_AVAILABLE:
        return _load_segy_stub(segy_path)

    _locs = byte_locs or {"iline": 189, "xline": 193}
    with segyio.open(str(segy_path), "r", iline=_locs["iline"], xline=_locs["xline"]) as f:
        segyio.tools.wrap(f)
        cube = segyio.tools.cube(f)           # (n_inlines, n_crosslines, n_samples)
        dt_us = segyio.tools.dt(f)            # sample interval in microseconds
        il_start = f.ilines[0]
        xl_start = f.xlines[0]

    logger.info("Loaded SEG-Y: shape %s, dt=%.1f ms", cube.shape, dt_us / 1000)
    return SeismicSurvey(
        data=cube,
        sample_rate_ms=dt_us / 1000.0,
        inline_start=il_start,
        crossline_start=xl_start,
        segy_path=segy_path,
    )


def _load_segy_stub(segy_path: Path) -> SeismicSurvey:
    """Stub: returns a synthetic mini-cube for testing without segyio."""
    logger.warning("Using synthetic SEG-Y stub — install segyio for real data.")
    rng = np.random.default_rng(42)
    cube = rng.standard_normal((50, 50, 500)).astype(np.float32)
    return SeismicSurvey(data=cube, sample_rate_ms=2.0, inline_start=1000, crossline_start=1000)


# ---------------------------------------------------------------------------
# Step 2: Preprocessing
# ---------------------------------------------------------------------------

def preprocess(survey: SeismicSurvey,
               freq_low_hz: float = 8.0,
               freq_high_hz: float = 80.0,
               agc_window_samples: int = 100) -> SeismicSurvey:
    """
    Standard pre-processing pipeline before ML inference:

        1. Bandpass filter (Butterworth) — suppress low-frequency swell noise
           and high-frequency acquisition noise.
        2. Trace-wise AGC (Automatic Gain Control) — normalise amplitude
           envelope variations with depth so the CNN sees consistent input
           amplitude statistics. Windows of 100–200 samples (200–400 ms at 2 ms)
           are typical.
        3. Clip to [-3, +3] standard deviations — prevents outlier amplitudes
           from dominating model activations.

    Note: preprocessing parameters significantly affect model output. A
    model trained on AGC-normalised data must be applied to AGC-normalised
    data. Mismatched preprocessing is one of the primary causes of poor
    out-of-basin generalisation. [VERIFY: preprocessing sensitivity studies]
    """
    data = survey.data.copy().astype(np.float32)
    nyq = 0.5 / (survey.sample_rate_ms / 1000.0)  # Hz
    b, a = signal.butter(4, [freq_low_hz / nyq, freq_high_hz / nyq], btype="band")

    # Apply bandpass along the time axis (axis=2)
    data = signal.sosfiltfilt(signal.butter(4, [freq_low_hz / nyq, freq_high_hz / nyq],
                                              btype="band", output="sos"),
                               data, axis=2)

    # Trace-wise AGC: divide each trace by a running RMS envelope
    for il in range(data.shape[0]):
        for xl in range(data.shape[1]):
            trace = data[il, xl, :]
            rms_env = _running_rms(trace, agc_window_samples)
            rms_env = np.maximum(rms_env, 1e-6)  # avoid division by zero
            data[il, xl, :] = trace / rms_env

    # Clip outliers
    data = np.clip(data, -3.0, 3.0)

    logger.info("Preprocessing complete: bandpass %.0f–%.0f Hz, AGC window %d samples",
                freq_low_hz, freq_high_hz, agc_window_samples)
    return SeismicSurvey(
        data=data,
        sample_rate_ms=survey.sample_rate_ms,
        inline_start=survey.inline_start,
        crossline_start=survey.crossline_start,
        segy_path=survey.segy_path,
    )


def _running_rms(trace: np.ndarray, window: int) -> np.ndarray:
    """Compute running RMS envelope with half-window padding."""
    sq = trace ** 2
    kernel = np.ones(window) / window
    return np.sqrt(np.convolve(sq, kernel, mode="same"))


# ---------------------------------------------------------------------------
# Step 3: Horizon picking — U-Net inference with Monte Carlo dropout
# ---------------------------------------------------------------------------

def pick_horizons(survey: SeismicSurvey,
                  model_path: Optional[Path] = None,
                  n_mc_samples: int = 20,
                  patch_size: tuple[int, int] = (64, 64)) -> list[InterpretedHorizon]:
    """
    AI-assisted horizon picking using a U-Net architecture.

    Architecture note:
        The U-Net (Ronneberger et al. 2015) encoder-decoder structure is the
        most widely adopted architecture for seismic segmentation tasks. It
        learns to assign each time sample on each trace a probability of
        belonging to a specific stratigraphic horizon. The decoder's skip
        connections preserve high-frequency spatial detail that would be
        lost in a plain encoder.

    Uncertainty quantification — Monte Carlo dropout:
        Standard U-Net inference gives a single deterministic pick. To
        produce calibrated uncertainty estimates (which satisfy the
        "reliable technology" audit requirement more convincingly), we use
        MC dropout: dropout layers remain active at inference, and the model
        is run n_mc_samples times on the same input. The variance across
        samples is a proxy for epistemic (model) uncertainty. This is a
        well-established approximation to Bayesian deep learning
        [Gal & Ghahramani 2016].

    Cost note: 20 MC samples = 20× single-pass inference compute.
        For a 500 km² survey, single-pass GPU inference ≈ 0.5–2 GPU-hours;
        MC dropout at n=20 ≈ 10–40 GPU-hours. [VERIFY]

    Returns:
        A list of InterpretedHorizon objects, one per detected reflector.
        Each carries a per-sample confidence score and 1-sigma uncertainty
        in milliseconds TWT.
    """
    if not TORCH_AVAILABLE or model_path is None:
        logger.warning("Returning stub horizon picks — torch not available or no model path.")
        return _horizon_stub(survey)

    model = _load_unet(model_path)
    model.train()  # keep dropout active for MC inference

    n_il, n_xl, n_t = survey.shape
    all_logits = np.zeros((n_mc_samples, n_il, n_xl, n_t), dtype=np.float32)

    with torch.no_grad():
        for mc_run in range(n_mc_samples):
            for il_start in range(0, n_il, patch_size[0]):
                il_end = min(il_start + patch_size[0], n_il)
                for xl_start in range(0, n_xl, patch_size[1]):
                    xl_end = min(xl_start + patch_size[1], n_xl)
                    patch = survey.data[il_start:il_end, xl_start:xl_end, :]
                    tensor = torch.from_numpy(patch).unsqueeze(0).unsqueeze(0)  # (1,1,IL,XL,T)
                    logit = model(tensor).squeeze().cpu().numpy()
                    all_logits[mc_run, il_start:il_end, xl_start:xl_end, :] = logit

    probs = _sigmoid(all_logits)  # (n_mc, n_il, n_xl, n_t)
    mean_prob = probs.mean(axis=0)
    std_prob = probs.std(axis=0)

    # Convert probability volume to discrete horizon picks (argmax per trace)
    picks_t = mean_prob.argmax(axis=-1).astype(float)  # sample index
    twt_ms = picks_t * survey.sample_rate_ms
    confidence = mean_prob.max(axis=-1)
    uncertainty_ms = std_prob.max(axis=-1) * survey.sample_rate_ms * n_t

    return [InterpretedHorizon(
        name="horizon_01",
        twt_ms=twt_ms,
        confidence=confidence,
        uncertainty_ms=uncertainty_ms,
    )]


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -88, 88)))


def _horizon_stub(survey: SeismicSurvey) -> list[InterpretedHorizon]:
    """Return synthetic horizon at constant TWT for testing."""
    rng = np.random.default_rng(0)
    n_il, n_xl, _ = survey.shape
    base_twt = 1200.0  # ms
    noise = rng.normal(0, 10.0, (n_il, n_xl))
    return [InterpretedHorizon(
        name="horizon_01_stub",
        twt_ms=np.full((n_il, n_xl), base_twt) + noise,
        confidence=np.full((n_il, n_xl), 0.75),
        uncertainty_ms=np.abs(noise) * 0.5,
    )]


def _load_unet(model_path: Path):
    """Load a pretrained U-Net from a .pt checkpoint. Stub for illustration."""
    raise NotImplementedError(
        "Load your U-Net checkpoint here. "
        "Architecture must match training configuration (channel counts, depth, dropout rate). "
        "Use torch.load(model_path, map_location='cuda' if torch.cuda.is_available() else 'cpu')"
    )


# ---------------------------------------------------------------------------
# Step 4: Fault detection — 3D CNN
# ---------------------------------------------------------------------------

def detect_faults(survey: SeismicSurvey,
                  model_path: Optional[Path] = None,
                  fault_threshold: float = 0.5) -> FaultProbabilityVolume:
    """
    3D CNN-based fault detection producing a voxel-wise fault probability volume.

    Architecture note:
        3D CNNs process sub-cubes of the seismic volume and output a per-voxel
        fault probability. The FaultSeg3D architecture (Wu et al. 2019) is the
        most cited open reference implementation. Commercial platforms use
        variants with larger receptive fields and multi-scale inputs.

    Validation note:
        Fault detection has the highest commercial maturity of any seismic
        AI application. However, performance degrades in:
        - Low signal-to-noise surveys
        - Subseismic fault populations (below tuning thickness)
        - Carbonate or salt-associated fault systems dissimilar to training data

        A QC step comparing AI fault picks to well-to-well correlation
        evidence is strongly recommended before using fault picks to
        constrain a static reservoir model.

    Returns:
        FaultProbabilityVolume with voxel-wise probability [0, 1].
        Binary fault/no-fault surface can be obtained by thresholding at
        `fault_threshold` (default 0.5).
    """
    if not TORCH_AVAILABLE or model_path is None:
        logger.warning("Returning stub fault volume — torch not available or no model path.")
        return _fault_stub(survey)

    # Stub: real implementation would tile the volume into sub-cubes,
    # run inference on each, and stitch the probability output.
    raise NotImplementedError(
        "Load your 3D CNN fault detection model here. "
        "Process in overlapping sub-cubes (e.g. 128×128×128 samples) "
        "with at least 16-sample overlap to avoid boundary artefacts."
    )


def _fault_stub(survey: SeismicSurvey) -> FaultProbabilityVolume:
    """Return a synthetic fault probability volume for testing."""
    rng = np.random.default_rng(1)
    prob = rng.uniform(0.0, 0.3, survey.shape).astype(np.float32)
    # Add a synthetic planar fault signal
    n_il = survey.shape[0]
    prob[n_il // 3: n_il // 3 + 2, :, :] += 0.6
    return FaultProbabilityVolume(probability=np.clip(prob, 0, 1))


# ---------------------------------------------------------------------------
# Step 5: Seismic facies classification
# ---------------------------------------------------------------------------

def classify_facies(survey: SeismicSurvey,
                    horizons: list[InterpretedHorizon],
                    n_classes: int = 5,
                    model_path: Optional[Path] = None) -> np.ndarray:
    """
    Seismic facies classification in the zone between two picked horizons.

    Approach:
        1. Extract seismic traces within the interpreted interval (between
           top and base horizons, padded by ±10 ms).
        2. Normalise interval traces to unit energy (removes TWT-dependent
           amplitude variation).
        3. Apply a trained classifier. Options:
           - Self-supervised pre-training (contrastive learning on unlabelled
             seismic) followed by supervised fine-tuning on labelled facies.
             Requires fewer labelled examples; reduces annotation cost.
           - Supervised CNN trained on labelled facies examples.
             Requires geoscientist annotation of training samples.
        4. Return a 2D facies map (dominant facies class per trace).

    Cost note:
        Self-supervised pre-training substantially reduces the annotation
        burden for new basins — a significant indirect-cost saving relative
        to pure supervised approaches that require 1,000–10,000 annotated
        examples per new geological setting. [VERIFY with annotation studies]

    Returns:
        np.ndarray of shape (n_inlines, n_crosslines) with integer facies
        class labels [0, n_classes-1].
    """
    logger.info("Facies classification stub: returning random facies map.")
    rng = np.random.default_rng(2)
    n_il, n_xl = survey.shape[:2]
    # Stub: Gaussian-smoothed random field to simulate spatially coherent facies
    raw = rng.integers(0, n_classes, (n_il, n_xl)).astype(float)
    from scipy.ndimage import gaussian_filter
    smoothed = gaussian_filter(raw, sigma=5)
    return np.round(smoothed % n_classes).astype(np.int32)


# ---------------------------------------------------------------------------
# Step 6: QC — Edit rate estimation
# ---------------------------------------------------------------------------

def estimate_edit_rate(ai_horizon: InterpretedHorizon,
                       manual_horizon: InterpretedHorizon,
                       edit_threshold_ms: float = 10.0) -> float:
    """
    Compute the fraction of traces where the AI pick differs from a reference
    manual pick by more than `edit_threshold_ms` milliseconds.

    This is the primary KPI for measuring whether AI output quality is
    sufficient for a given deployment. The ValorAI KPI model
    (docs/metrics/subsurface-ai-kpis.json) recommends tracking this
    metric during the POC before committing to enterprise rollout.

    A threshold of 10 ms at 2 ms sample rate represents a 5-sample
    discrepancy — roughly half of typical seismic tuning thickness. Values
    above ~30–40% suggest the model is not generalising reliably to this
    survey and requires retraining before production use.

    Returns:
        float: fraction of traces with |AI - manual| > edit_threshold_ms
    """
    diff_ms = np.abs(ai_horizon.twt_ms - manual_horizon.twt_ms)
    edit_rate = (diff_ms > edit_threshold_ms).mean()
    logger.info("Estimated edit rate: %.1f%% (threshold %.0f ms)", edit_rate * 100, edit_threshold_ms)
    return float(edit_rate)


# ---------------------------------------------------------------------------
# Step 7: Export — standard exchange formats
# ---------------------------------------------------------------------------

def export_horizon_xyz(horizon: InterpretedHorizon,
                       survey: SeismicSurvey,
                       output_path: Path) -> None:
    """
    Export horizon as an ASCII XYZ file (X, Y, TWT_ms, Confidence,
    Uncertainty_ms) for import into Petrel, Kingdom, or OpendTect.

    The uncertainty and confidence columns are included deliberately:
    the audit trail requirement (see use-case governance section) is
    better served by outputs that carry their own epistemic metadata
    rather than presenting a single picked value.
    """
    n_il, n_xl = horizon.twt_ms.shape
    rows = []
    for i in range(n_il):
        for j in range(n_xl):
            x = float(survey.cdp_x[i, j]) if survey.cdp_x is not None else float(i)
            y = float(survey.cdp_y[i, j]) if survey.cdp_y is not None else float(j)
            rows.append((x, y,
                         horizon.twt_ms[i, j],
                         horizon.confidence[i, j],
                         horizon.uncertainty_ms[i, j]))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fh:
        fh.write("# X  Y  TWT_ms  Confidence  Uncertainty_ms\n")
        fh.write(f"# Provenance: {horizon.provenance}\n")
        fh.write(f"# Horizon: {horizon.name}\n")
        for row in rows:
            fh.write(f"{row[0]:.2f}  {row[1]:.2f}  {row[2]:.3f}  {row[3]:.4f}  {row[4]:.3f}\n")

    logger.info("Exported %d picks to %s", len(rows), output_path)


# ---------------------------------------------------------------------------
# Entry point — end-to-end POC pipeline
# ---------------------------------------------------------------------------

def run_pipeline(segy_path: Path,
                 output_dir: Path,
                 model_dir: Optional[Path] = None) -> None:
    """
    End-to-end proof-of-concept pipeline:
        load → preprocess → pick horizons → detect faults → classify facies → export

    In a production deployment, each step would be parameterised via a config
    file, executed on a GPU-enabled HPC node or cloud instance, and version-
    controlled so that the model versions used for any interpreted dataset can
    be traced for audit purposes.

    Audit traceability note:
        For reserves-reporting compliance, log:
        - segy_path + file hash
        - model checkpoint path + hash for each model used
        - preprocessing parameters (bandpass, AGC window)
        - MC dropout samples (n_mc_samples)
        - git commit hash of this script
        Write these to an audit_log.json alongside each output file.
    """
    logger.info("=== Seismic AI Pipeline: start ===")
    logger.info("Input: %s", segy_path)

    # 1. Load
    survey = load_segy(segy_path)

    # 2. Preprocess
    survey_pp = preprocess(survey)

    # 3. Horizon picking with MC-dropout uncertainty
    horizon_model = model_dir / "unet_horizon.pt" if model_dir else None
    horizons = pick_horizons(survey_pp, model_path=horizon_model, n_mc_samples=20)

    # 4. Fault detection
    fault_model = model_dir / "cnn_fault.pt" if model_dir else None
    fault_vol = detect_faults(survey_pp, model_path=fault_model)

    # 5. Facies classification (between first two horizons if available)
    facies_model = model_dir / "facies_clf.pt" if model_dir else None
    facies = classify_facies(survey_pp, horizons, model_path=facies_model)

    # 6. QC — edit rate (requires a reference manual horizon; skipped here)
    logger.info("QC: edit-rate estimation requires a reference manual horizon — skipping in POC mode.")

    # 7. Export
    output_dir.mkdir(parents=True, exist_ok=True)
    for h in horizons:
        export_horizon_xyz(h, survey, output_dir / f"{h.name}.xyz")
    logger.info("Fault probability volume: shape %s, mean prob %.3f",
                fault_vol.probability.shape, fault_vol.probability.mean())
    logger.info("Facies map: unique classes %s", np.unique(facies).tolist())
    logger.info("=== Pipeline complete. Outputs in %s ===", output_dir)


if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")

    parser = argparse.ArgumentParser(description="Seismic AI interpretation POC pipeline")
    parser.add_argument("segy", type=Path, help="Input SEG-Y file path")
    parser.add_argument("output", type=Path, help="Output directory for picks and logs")
    parser.add_argument("--models", type=Path, default=None,
                        help="Directory containing model checkpoints (optional)")
    args = parser.parse_args()

    run_pipeline(args.segy, args.output, args.models)
