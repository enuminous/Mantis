from mantis import MantisMonitor, MantisConfig
import random

rng = random.Random(7)
m = MantisMonitor(MantisConfig(window=12, baseline_points=30, alarm_threshold=1.5, min_coherence=0.66))

x = 0.0
for t in range(80):
    rho = 0.2 if t < 40 else min(0.95, 0.2 + (t-40)*0.018)
    noise = 0.1 if t < 40 else 0.1 + (t-40)*0.004
    x = rho*x + rng.gauss(0, noise)
    out = m.update(x)
    if out.get("ready"):
        print(t, out["state"], round(out["precursor_score"],3), out["alarm"])
