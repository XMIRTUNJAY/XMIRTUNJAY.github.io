#!/usr/bin/env python3
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Event:
    id: str
    trade_date: str
    amount: float
    currency: str


def ingest() -> List[Event]:
    return [
        Event("T1", "2026-03-01", 125000.0, "USD"),
        Event("T2", "2026-03-01", 95500.0, "EUR"),
        Event("T3", "2026-03-01", 210000.0, "USD"),
    ]


def transform(events: List[Event], fx: Dict[str, float]) -> List[dict]:
    records = []
    for e in events:
        amount_usd = e.amount * fx[e.currency]
        records.append({"id": e.id, "trade_date": e.trade_date, "amount_usd": round(amount_usd, 2)})
    return records


def quality_check(records: List[dict]) -> List[dict]:
    return [r for r in records if r["amount_usd"] > 0]


def sink(records: List[dict]) -> None:
    total = sum(r["amount_usd"] for r in records)
    print(f"Loaded {len(records)} records; gross USD amount={total:.2f}")


if __name__ == "__main__":
    fx_table = {"USD": 1.0, "EUR": 1.08}
    loaded = quality_check(transform(ingest(), fx_table))
    sink(loaded)
