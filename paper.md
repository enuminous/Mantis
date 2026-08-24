# MANTIS: Model Anticipation of Nonlinear Threats and Intervention States

## Abstract

MANTIS is an experimental sequential monitoring framework for identifying precursor structure near nonlinear regime transitions. It combines rolling variance, lag-1 autocorrelation, recovery behavior, and curvature-like indicators into a calibrated precursor score and explicitly separates detection from intervention-state estimation.

## 1. Motivation

Some systems do not degrade smoothly.

Near a critical transition, local dynamics may change before the final observable failure. MANTIS targets these changes.

## 2. Model

For observed state `x_t`, estimate rolling:

- variance
- lag-1 autocorrelation
- recovery coefficient
- second-difference magnitude

Each metric is normalized against a stable baseline.

Composite precursor score:

`P_t = mean(max(0,Z_i))`

Indicator coherence:

`K_t = fraction of indicators moving in warning direction`

Alarm:

`P_t > theta_P and K_t > theta_K`

## 3. Primary endpoint

Lead time to known transition at matched false-alarm rate.

## 4. Baselines

- CUSUM
- EWMA
- Bayesian change-point detection
- Kalman residual monitoring
- autoregressive stability estimation
- critical-slowing-only monitors
- tuned ensembles

## 5. Ablations

- remove autocorrelation
- remove variance
- remove curvature
- remove recovery estimate
- remove coherence requirement
- remove baseline standardization
- remove recursive history

## 6. Falsification

If simpler change-point or state-space methods match MANTIS at equal false-alarm rate and information access, its added complexity is not justified.

## 7. Claim boundary

MANTIS is a candidate early-warning framework. A warning score does not prove that a bifurcation or catastrophic transition is imminent.
