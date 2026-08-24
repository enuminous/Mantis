import unittest
from mantis import MantisMonitor, MantisConfig

class TestMantis(unittest.TestCase):
    def test_calibration_state(self):
        m = MantisMonitor(MantisConfig(window=5, baseline_points=10))
        out = m.update(0.0)
        self.assertFalse(out["ready"])

    def test_metrics_after_baseline(self):
        m = MantisMonitor(MantisConfig(window=5, baseline_points=10, alarm_threshold=99))
        for x in [0,0.1,-0.1,0.05,-0.05,0.1,-0.1,0.0,0.05,-0.05]:
            out = m.update(x)
        out = m.update(0.1)
        self.assertTrue(out["ready"])
        self.assertIn("z_scores", out)

    def test_constant_series_no_alarm(self):
        m = MantisMonitor(MantisConfig(window=5, baseline_points=10, alarm_threshold=1.0))
        alarm = False
        for _ in range(20):
            out = m.update(0.0)
            alarm = alarm or out.get("alarm",False)
        self.assertFalse(alarm)

if __name__ == "__main__":
    unittest.main()
