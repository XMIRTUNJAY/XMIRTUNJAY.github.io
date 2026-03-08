#!/usr/bin/env python3
import argparse
import csv
from typing import Dict, List


def ratio(value: float, base: float) -> float:
    return 0.0 if base == 0 else (value / base) * 100


def evaluate(row: Dict[str, str]) -> Dict[str, float]:
    revenue = float(row["revenue"])
    gross_profit = revenue - float(row["cogs"])
    operating_income = float(row["operating_income"])
    net_income = float(row["net_income"])
    fcf = float(row["free_cash_flow"])
    debt = float(row["total_debt"])
    ebitda = float(row["ebitda"])

    return {
        "gross_margin": ratio(gross_profit, revenue),
        "operating_margin": ratio(operating_income, revenue),
        "net_margin": ratio(net_income, revenue),
        "fcf_margin": ratio(fcf, revenue),
        "debt_to_ebitda": 0.0 if ebitda == 0 else debt / ebitda,
    }


def read_rows(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    rows = read_rows(args.input)
    for row in rows:
        metrics = evaluate(row)
        print(f"\n{row['company']}")
        print(f"  Gross margin: {metrics['gross_margin']:.2f}%")
        print(f"  Operating margin: {metrics['operating_margin']:.2f}%")
        print(f"  Net margin: {metrics['net_margin']:.2f}%")
        print(f"  FCF margin: {metrics['fcf_margin']:.2f}%")
        print(f"  Debt/EBITDA: {metrics['debt_to_ebitda']:.2f}x")


if __name__ == "__main__":
    main()
