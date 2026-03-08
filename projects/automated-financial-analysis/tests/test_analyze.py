import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import analyze  # noqa: E402


class FinancialAnalysisTests(unittest.TestCase):
    def test_evaluate_returns_expected_keys(self):
        row = {
            "company": "TestCo",
            "revenue": "1000",
            "cogs": "400",
            "operating_income": "200",
            "net_income": "120",
            "free_cash_flow": "150",
            "total_debt": "300",
            "ebitda": "180",
        }
        result = analyze.evaluate(row)
        self.assertAlmostEqual(result["gross_margin"], 60.0)
        self.assertAlmostEqual(result["operating_margin"], 20.0)
        self.assertAlmostEqual(result["net_margin"], 12.0)
        self.assertAlmostEqual(result["fcf_margin"], 15.0)
        self.assertAlmostEqual(result["debt_to_ebitda"], 1.6666666, places=4)

    def test_ratio_handles_zero_base(self):
        self.assertEqual(analyze.ratio(10.0, 0.0), 0.0)


if __name__ == "__main__":
    unittest.main()
