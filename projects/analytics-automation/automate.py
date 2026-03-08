#!/usr/bin/env python3
from functools import reduce
from typing import Callable, Iterable, List


def compose(*funcs: Callable):
    return lambda x: reduce(lambda acc, f: f(acc), funcs, x)


def clean(values: Iterable[float]) -> List[float]:
    return [v for v in values if v is not None and v >= 0]


def normalize(values: List[float]) -> List[float]:
    if not values:
        return []
    peak = max(values)
    return [round(v / peak, 3) for v in values]


def rolling_mean(values: List[float], window: int = 3) -> List[float]:
    if len(values) < window:
        return values
    return [round(sum(values[i:i + window]) / window, 3) for i in range(len(values) - window + 1)]


def main() -> None:
    raw = [12, 18, None, -2, 21, 30, 27]
    pipeline = compose(clean, normalize, lambda xs: rolling_mean(xs, 3))
    print(pipeline(raw))


if __name__ == "__main__":
    main()
