import random
from mantis import MantisMonitor, MantisConfig

def generate(seed=30, stable=60, ramp=80):
    rng = random.Random(seed)
    xs = []
    x = 0.0
    for t in range(stable+ramp):
        if t < stable:
            rho = 0.25
            noise = 0.18
        else:
            f = (t-stable)/max(1,ramp-1)
            rho = 0.25 + 0.70*f
            noise = 0.18 + 0.22*f
        x = rho*x + rng.gauss(0,noise)
        xs.append(x)
    transition_time = stable+ramp-1
    return xs, transition_time

def run(seed=30):
    xs, transition = generate(seed)
    m = MantisMonitor(MantisConfig(window=20, baseline_points=50, alarm_threshold=2.0, min_coherence=0.66))
    alarm_t = None
    peak = 0.0
    for t,x in enumerate(xs):
        out = m.update(x)
        peak = max(peak, out.get("precursor_score",0.0))
        if out.get("alarm") and alarm_t is None:
            alarm_t = t
    return {
        "seed": seed,
        "alarm_time": alarm_t,
        "transition_time": transition,
        "lead_time": None if alarm_t is None else transition-alarm_t,
        "peak_score": peak
    }

if __name__ == "__main__":
    for seed in [11,23,30,46,59]:
        print(run(seed))
