import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import pipeline  # noqa: E402


class DataPipelineTests(unittest.TestCase):
    def test_transform_and_quality_check(self):
        events = pipeline.ingest()
        fx = {"USD": 1.0, "EUR": 1.1}
        records = pipeline.transform(events, fx)
        self.assertEqual(len(records), 3)
        cleaned = pipeline.quality_check(records)
        self.assertEqual(len(cleaned), 3)
        self.assertTrue(all(r["amount_usd"] > 0 for r in cleaned))


if __name__ == "__main__":
    unittest.main()
