import json
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import engine  # noqa: E402


class StockEngineTests(unittest.TestCase):
    def setUp(self):
        self.stocks = json.loads((BASE / "sample_stocks.json").read_text(encoding="utf-8"))

    def test_rank_stocks_returns_top_n(self):
        ranked = engine.rank_stocks(self.stocks, 2)
        self.assertEqual(len(ranked), 2)
        self.assertGreaterEqual(ranked[0].score, ranked[1].score)

    def test_score_bounds(self):
        for stock in self.stocks:
            scored = engine.score_stock(stock)
            self.assertGreaterEqual(scored.score, 0)
            self.assertLessEqual(scored.score, 100)


if __name__ == "__main__":
    unittest.main()
