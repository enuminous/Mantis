# MANTIS — EFMW Zoo #30

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
