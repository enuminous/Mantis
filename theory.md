# MANTIS Theory

## 1. Problem

Some failures are not gradual in output space.

A system may appear acceptable until a control parameter crosses a threshold, after which behavior changes abruptly.

Examples include:
- control instability,
- cascading overload,
- phase transitions,
- runaway feedback,
- abrupt policy collapse,
- sudden mode switching.

MANTIS targets precursor structure before the transition.

## 2. Hidden regime variable

Let system state be `x_t` and a slowly changing control parameter be `mu_t`.

A generic nonlinear system:

`x_{t+1} = F(x_t, mu_t) + epsilon_t`

A critical transition may occur near:

`mu_t = mu_c`

## 3. Critical slowing down

Near some bifurcations, perturbations recover more slowly.

Let recovery coefficient be `rho_t`.

Candidate warning:

`rho_t -> 1`

for discrete-time systems.

## 4. Variance escalation

As stability weakens, local variance may increase:

`Var(x_t window) up`

## 5. Lag-1 autocorrelation

Candidate indicator:

`AC1_t = corr(x_t, x_{t-1})`

Increasing `AC1` can indicate slower recovery.

## 6. Curvature / nonlinear acceleration

Define first difference:

`v_t = x_t - x_{t-1}`

Second difference:

`a_t = v_t - v_{t-1}`

Rapid growth in `|a_t|` can indicate nonlinear departure from baseline trajectory.

## 7. Composite precursor score

A candidate MANTIS score:

`P_t = w1*Z_AC1 + w2*Z_VAR + w3*Z_REC + w4*Z_CURV`

where each term is normalized against a baseline distribution.

## 8. Intervention window

Let `T_c` denote estimated transition time.

Define intervention horizon:

`W_t = max(0, T_c - t)`

A practical intervention score can incorporate both proximity and confidence:

`I_t = confidence_t / (W_t + eps)`

The objective is not merely to predict failure but to identify when intervention remains both necessary and feasible.

## 9. EFMW interpretation

The EFMW-inspired aspect is recursive preservation of:
- state trajectory,
- local stability,
- recovery dynamics,
- cross-indicator coherence,
- intervention history.

## 10. Falsifiable prediction

MANTIS should add value when:
- transitions are nonlinear,
- precursors appear in dynamics before raw magnitude,
- recovery slows before failure,
- multiple indicators cohere.

If standard change-point, CUSUM, or state-space methods match lead time at matched false-alarm rate, the added framework is not justified.
