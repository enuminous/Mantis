# Transition Model

## Reference nonlinear process

A simple cubic normal-form process can be used for synthetic experiments:

`x_{t+1} = x_t + dt*(mu_t - x_t^2) + noise`

As `mu_t` approaches a critical region, the local dynamics change.

## Observation window

For rolling window `W`, calculate:

- mean
- variance
- lag-1 autocorrelation
- mean absolute second difference
- recovery estimate after perturbation when available

## Baseline calibration

All precursor terms should be standardized against a stable calibration period.

For metric `m`:

`Z_m = (m_t - mean_baseline_m) / std_baseline_m`

## Composite alarm

`Alarm_t = 1[P_t > theta_P and K_t > theta_K]`

where `K_t` measures agreement among precursor indicators.

## Intervention state

Candidate state labels:

- STABLE
- WATCH
- PRECURSOR
- INTERVENE
- TRANSITION
- RECOVERY

## Lead time

`LeadTime = T_transition - T_first_intervention_alert`

must be evaluated at matched false-alarm rate.
