# MANTIS — EFMW Zoo #30

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Mantis) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Model Anticipation of Nonlinear Threats and Intervention States**

MANTIS is an experimental EFMW-inspired framework for detecting approaching nonlinear transitions and identifying intervention windows before a monitored system crosses into a hazardous regime.

## Core question

> Is the system merely fluctuating, or is it approaching a qualitative change in behavior where small additional stress could produce a large failure?

MANTIS focuses on early-warning structure near regime shifts.

## Primary outputs

- precursor score
- nonlinear-transition proximity
- critical-slowing indicator
- variance escalation
- recovery-rate degradation
- intervention-window score
- false-alarm calibrated alert state

## Repository contents

- `theory.md`
- `architecture.md`
- `transition_model.md`
- `limitations.md`
- `mantis.py`
- `benchmark.py`
- `ablations.py`
- `test_mantis.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_mantis.py
```

## Zoo position

BEAVER #29 evaluates whether repairs are bounded and safe.

**MANTIS #30 asks whether the system can recognize the shrinking interval in which intervention is still effective before a nonlinear transition occurs.**
