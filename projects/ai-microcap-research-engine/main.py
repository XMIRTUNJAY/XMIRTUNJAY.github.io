#!/usr/bin/env python3
"""AI Microcap Research Engine.

A deterministic, interview-friendly research engine that combines
fundamental and technical factors with headline sentiment to rank
microcap opportunities and generate an analyst-style report.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class ScoredCompany:
    ticker: str
    company: str
    sector: str
    conviction_score: float
    quality_band: str
    thesis: str
    factors: Dict[str, float]


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def scale(value: float, in_min: float, in_max: float) -> float:
    if in_max == in_min:
        return 0.0
    return clamp((value - in_min) / (in_max - in_min), 0.0, 1.0)


def valuation_factor(pe: float, pb: float) -> float:
    pe_score = 1.0 - scale(pe, 8.0, 35.0)
    pb_score = 1.0 - scale(pb, 1.0, 6.0)
    return (pe_score * 0.6) + (pb_score * 0.4)


def growth_factor(rev_growth: float, eps_growth: float) -> float:
    rev_score = scale(rev_growth, -0.1, 0.5)
    eps_score = scale(eps_growth, -0.2, 0.5)
    return (rev_score * 0.55) + (eps_score * 0.45)


def quality_factor(roe: float, debt_to_equity: float, filing_quality: float) -> float:
    roe_score = scale(roe, 0.0, 0.3)
    leverage_score = 1.0 - scale(debt_to_equity, 0.0, 1.5)
    filing_score = clamp(filing_quality, 0.0, 1.0)
    return (roe_score * 0.45) + (leverage_score * 0.35) + (filing_score * 0.2)


def momentum_factor(price_change_6m: float, relative_strength: float) -> float:
    perf_score = scale(price_change_6m, -0.25, 0.6)
    rs_score = scale(relative_strength, 20.0, 90.0)
    return (perf_score * 0.6) + (rs_score * 0.4)


def risk_penalty(volatility: float, beta: float, avg_daily_volume: float) -> float:
    vol_pen = scale(volatility, 0.25, 0.8)
    beta_pen = scale(beta, 0.8, 2.0)
    liq_pen = 1.0 - scale(avg_daily_volume, 60000.0, 300000.0)
    return (vol_pen * 0.45) + (beta_pen * 0.35) + (liq_pen * 0.2)


def sentiment_factor(sentiment: float) -> float:
    return scale(sentiment, -1.0, 1.0)


def conviction_score(row: dict, sentiment: float) -> Tuple[float, Dict[str, float]]:
    factors = {
        "valuation": valuation_factor(row["pe"], row["pb"]),
        "growth": growth_factor(row["revenue_growth_yoy"], row["eps_growth_yoy"]),
        "quality": quality_factor(row["roe"], row["debt_to_equity"], row["filing_quality"]),
        "momentum": momentum_factor(row["price_change_6m"], row["relative_strength"]),
        "sentiment": sentiment_factor(sentiment),
        "risk_penalty": risk_penalty(row["volatility"], row["beta"], row["avg_daily_volume"]),
    }

    weighted = (
        factors["valuation"] * 0.2
        + factors["growth"] * 0.25
        + factors["quality"] * 0.2
        + factors["momentum"] * 0.2
        + factors["sentiment"] * 0.15
        - factors["risk_penalty"] * 0.2
    )

    base_score = clamp(weighted, 0.0, 1.0) * 100
    if row.get("insider_buying"):
        base_score += 4

    return clamp(base_score, 0.0, 100.0), factors


def quality_band(score: float) -> str:
    if score >= 75:
        return "High Conviction"
    if score >= 60:
        return "Watchlist"
    return "Speculative"


def build_thesis(row: dict, sentiment_headline: str, score: float) -> str:
    catalyst = row.get("catalyst", "No catalyst provided")
    return (
        f"{row['ticker']} ({row['company']}) shows {row['revenue_growth_yoy']:.0%} revenue growth with "
        f"ROE {row['roe']:.0%}. Catalyst: {catalyst}. Market signal: {sentiment_headline}. "
        f"Engine score={score:.1f}."
    )


def rank_companies(universe: List[dict], sentiments: Dict[str, dict]) -> List[ScoredCompany]:
    ranked: List[ScoredCompany] = []
    for row in universe:
        ticker = row["ticker"]
        sent = sentiments.get(ticker, {"sentiment": 0.0, "headline": "No recent headline context"})
        score, factors = conviction_score(row, sent["sentiment"])
        ranked.append(
            ScoredCompany(
                ticker=ticker,
                company=row["company"],
                sector=row["sector"],
                conviction_score=score,
                quality_band=quality_band(score),
                thesis=build_thesis(row, sent["headline"], score),
                factors=factors,
            )
        )
    return sorted(ranked, key=lambda x: x.conviction_score, reverse=True)


def to_markdown_report(scored: List[ScoredCompany], top_n: int) -> str:
    lines = [
        "# AI Microcap Research Engine Report",
        "",
        "## Top Picks",
        "",
    ]
    for i, company in enumerate(scored[:top_n], start=1):
        lines.extend(
            [
                f"### {i}. {company.ticker} — {company.company}",
                f"- Sector: {company.sector}",
                f"- Conviction score: **{company.conviction_score:.1f}/100** ({company.quality_band})",
                f"- Thesis: {company.thesis}",
                (
                    f"- Factors: valuation={company.factors['valuation']:.2f}, "
                    f"growth={company.factors['growth']:.2f}, quality={company.factors['quality']:.2f}, "
                    f"momentum={company.factors['momentum']:.2f}, sentiment={company.factors['sentiment']:.2f}, "
                    f"risk_penalty={company.factors['risk_penalty']:.2f}"
                ),
                "",
            ]
        )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI Microcap Research Engine")
    parser.add_argument("--universe", default="data/microcap_universe.json", help="Path to universe JSON")
    parser.add_argument("--sentiment", default="data/news_sentiment.json", help="Path to sentiment JSON")
    parser.add_argument("--top", type=int, default=3, help="Number of top picks in report")
    parser.add_argument("--output", default="output/report.md", help="Report output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = Path(__file__).parent

    universe = json.loads((base / args.universe).read_text(encoding="utf-8"))
    sentiments = json.loads((base / args.sentiment).read_text(encoding="utf-8"))

    scored = rank_companies(universe, sentiments)
    report = to_markdown_report(scored, args.top)

    out_path = base / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    print(f"Generated report: {out_path}")
    print("Top ranked tickers:", ", ".join(x.ticker for x in scored[: args.top]))


if __name__ == "__main__":
    main()
