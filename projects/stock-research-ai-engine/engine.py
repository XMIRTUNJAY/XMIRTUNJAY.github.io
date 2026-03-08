#!/usr/bin/env python3
import argparse
import json
from dataclasses import dataclass
from typing import List


@dataclass
class SignalResult:
    ticker: str
    score: int
    thesis: str


def score_stock(stock: dict) -> SignalResult:
    score = 50
    pe = stock.get("pe", 20)
    growth = stock.get("revenue_growth", 0)
    leverage = stock.get("debt_to_equity", 1)
    momentum = stock.get("price_change_6m", 0)
    insider = stock.get("insider_buying", False)

    if pe < 15:
        score += 12
    elif pe > 28:
        score -= 8

    if growth > 0.2:
        score += 14
    elif growth < 0.05:
        score -= 10

    if leverage < 0.5:
        score += 10
    elif leverage > 1.2:
        score -= 12

    if momentum > 0.2:
        score += 8
    elif momentum < -0.05:
        score -= 6

    if insider:
        score += 6

    score = max(0, min(100, score))
    thesis = build_thesis(stock, score)
    return SignalResult(stock["ticker"], score, thesis)


def build_thesis(stock: dict, score: int) -> str:
    tone = "high-conviction" if score >= 75 else "watchlist" if score >= 60 else "low-conviction"
    return (
        f"{stock['ticker']} is a {tone} candidate with revenue growth at {stock['revenue_growth']:.0%}, "
        f"P/E {stock['pe']}, and debt/equity {stock['debt_to_equity']}."
    )


def rank_stocks(stocks: List[dict], top_n: int) -> List[SignalResult]:
    ranked = sorted((score_stock(s) for s in stocks), key=lambda r: r.score, reverse=True)
    return ranked[:top_n]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        stocks = json.load(f)

    for item in rank_stocks(stocks, args.top):
        print(f"{item.ticker}: {item.score}")
        print(f"  - {item.thesis}")


if __name__ == "__main__":
    main()
