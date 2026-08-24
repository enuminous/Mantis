from dataclasses import dataclass
from collections import deque
from typing import Optional, Dict
import math
from statistics import mean, variance

@dataclass
class MantisConfig:
    window: int = 20
    baseline_points: int = 40
    alarm_threshold: float = 2.0
    min_coherence: float = 0.5

class MantisMonitor:
    def __init__(self, config: Optional[MantisConfig] = None):
        self.config = config or MantisConfig()
        self.values = []
        self.baseline_metrics = None

    def _metrics(self, xs):
        if len(xs) < 4:
            return {"var":0.0, "ac1":0.0, "curv":0.0}

        v = variance(xs) if len(xs) > 1 else 0.0

        x0 = xs[:-1]
        x1 = xs[1:]
        m0 = mean(x0)
        m1 = mean(x1)
        num = sum((a-m0)*(b-m1) for a,b in zip(x0,x1))
        den0 = math.sqrt(sum((a-m0)**2 for a in x0))
        den1 = math.sqrt(sum((b-m1)**2 for b in x1))
        ac1 = num/(den0*den1) if den0 > 0 and den1 > 0 else 0.0

        diffs = [xs[i]-xs[i-1] for i in range(1,len(xs))]
        second = [diffs[i]-diffs[i-1] for i in range(1,len(diffs))]
        curv = mean(abs(x) for x in second) if second else 0.0

        return {"var":v, "ac1":ac1, "curv":curv}

    def _z(self, value, mu, sigma):
        if sigma <= 1e-12:
            return 0.0
        return (value-mu)/sigma

    def update(self, x: float):
        self.values.append(float(x))

        if len(self.values) == self.config.baseline_points:
            w = self.config.window
            samples = []
            for i in range(w, len(self.values)+1):
                samples.append(self._metrics(self.values[i-w:i]))
            self.baseline_metrics = {}
            for k in ["var","ac1","curv"]:
                vals = [m[k] for m in samples]
                mu = mean(vals)
                sd = math.sqrt(sum((v-mu)**2 for v in vals)/max(1,len(vals)-1))
                self.baseline_metrics[k] = (mu,sd)

        if len(self.values) < self.config.window:
            return {
                "ready": False,
                "precursor_score": 0.0,
                "coherence": 0.0,
                "alarm": False,
                "state": "CALIBRATING"
            }

        current = self._metrics(self.values[-self.config.window:])

        if not self.baseline_metrics:
            return {
                "ready": False,
                "precursor_score": 0.0,
                "coherence": 0.0,
                "alarm": False,
                "state": "CALIBRATING",
                **current
            }

        zs = {}
        for k,v in current.items():
            mu,sd = self.baseline_metrics[k]
            zs[k] = self._z(v,mu,sd)

        positive = [1 if zs[k] > 0 else 0 for k in zs]
        coherence = sum(positive)/len(positive)
        precursor = mean(max(0.0,z) for z in zs.values())

        alarm = precursor >= self.config.alarm_threshold and coherence >= self.config.min_coherence
        state = "INTERVENE" if alarm else ("PRECURSOR" if precursor >= self.config.alarm_threshold*0.6 else "STABLE")

        return {
            "ready": True,
            "precursor_score": precursor,
            "coherence": coherence,
            "alarm": alarm,
            "state": state,
            "variance": current["var"],
            "autocorrelation": current["ac1"],
            "curvature": current["curv"],
            "z_scores": zs,
        }
