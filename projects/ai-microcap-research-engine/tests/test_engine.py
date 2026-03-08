import json
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import main  # noqa: E402


class EngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.universe = json.loads((BASE / "data/microcap_universe.json").read_text(encoding="utf-8"))
        self.sentiment = json.loads((BASE / "data/news_sentiment.json").read_text(encoding="utf-8"))

    def test_scores_within_bounds(self):
        ranked = main.rank_companies(self.universe, self.sentiment)
        self.assertTrue(len(ranked) >= 3)
        for row in ranked:
            self.assertGreaterEqual(row.conviction_score, 0)
            self.assertLessEqual(row.conviction_score, 100)

    def test_report_contains_top_pick(self):
        ranked = main.rank_companies(self.universe, self.sentiment)
        report = main.to_markdown_report(ranked, 2)
        self.assertIn("## Top Picks", report)
        self.assertIn(ranked[0].ticker, report)


if __name__ == "__main__":
    unittest.main()
