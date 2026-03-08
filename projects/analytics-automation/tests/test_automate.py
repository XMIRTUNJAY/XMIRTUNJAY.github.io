import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import automate  # noqa: E402


class AnalyticsAutomationTests(unittest.TestCase):
    def test_pipeline_filters_and_normalizes(self):
        raw = [12, 18, None, -2, 21, 30, 27]
        pipeline = automate.compose(automate.clean, automate.normalize, lambda xs: automate.rolling_mean(xs, 3))
        self.assertEqual(pipeline(raw), [0.567, 0.767, 0.867])

    def test_empty_input(self):
        self.assertEqual(automate.clean([]), [])
        self.assertEqual(automate.normalize([]), [])


if __name__ == "__main__":
    unittest.main()
