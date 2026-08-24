# Limitations and Falsification

MANTIS is an experimental early-warning framework.

## Limitations

- Critical slowing does not precede every failure.
- Autocorrelation and variance can rise for unrelated reasons.
- Window length strongly affects metrics.
- Nonstationary noise can mimic precursor signals.
- Bifurcation assumptions may be wrong.
- Estimated intervention windows may be highly uncertain.

## Falsification criteria

MANTIS's central hypothesis is weakened if:

1. Tuned change-point methods match or outperform it.
2. Precursor indicators provide no lead-time gain.
3. Removing recursive state tracking causes no performance loss.
4. Indicator coherence does not improve false-alarm control.
5. Performance fails on held-out nonlinear systems.
6. Apparent gains vanish after matching false-alarm rate.

## Claim boundary

MANTIS estimates transition risk under a configured model. It does not prove that a bifurcation or catastrophic transition will occur.
