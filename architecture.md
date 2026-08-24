# MANTIS Architecture

## Pipeline

1. Observation Ingestor
2. Stable-Baseline Calibrator
3. Rolling Dynamics Analyzer
4. Recovery Estimator
5. Nonlinear Curvature Detector
6. Indicator Normalizer
7. Precursor Coherence Engine
8. Intervention Window Estimator
9. Alert Controller
10. Audit Logger

## Inputs

- time-series observations
- optional control parameters
- optional perturbation/recovery traces
- calibration interval
- alert thresholds

## Outputs

```json
{
  "precursor_score": 2.14,
  "variance_z": 1.21,
  "autocorrelation_z": 1.63,
  "curvature_z": 0.87,
  "indicator_coherence": 0.75,
  "state": "PRECURSOR",
  "alarm": true
}
```

## Design principle

MANTIS should not confuse large values with nonlinear transition risk.

The framework asks whether **dynamics are changing**, not merely whether measurements are high.

## Integration

WOLF can supply weak distributed precursor channels.

JELLYFISH can estimate what downstream cascade follows a transition.

BEAVER can evaluate candidate interventions.

ELEPHANT can preserve pre-transition and post-transition histories.
