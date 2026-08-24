from benchmark import generate
from mantis import MantisMonitor, MantisConfig

def run(full=True):
    xs, transition = generate(30)
    threshold = 2.0 if full else 999.0
    m = MantisMonitor(MantisConfig(window=20, baseline_points=50, alarm_threshold=threshold, min_coherence=0.66))
    alarm_t = None
    for t,x in enumerate(xs):
        out = m.update(x)
        if out.get("alarm") and alarm_t is None:
            alarm_t = t
    return alarm_t

if __name__ == "__main__":
    print("full alarm:", run(True))
    print("ablated/no precursor alert:", run(False))
