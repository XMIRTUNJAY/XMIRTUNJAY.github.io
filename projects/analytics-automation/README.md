# Analytics Automation

A lightweight functional-style transformation pipeline for reusable analytics preprocessing.

## What it does
- Cleans invalid values (`None`, negatives).
- Normalizes signal values to a 0..1 range.
- Applies rolling-window smoothing.

## Project layout

```text
analytics-automation/
├── automate.py
└── tests/
    └── test_automate.py
```

## Run

```bash
python3 automate.py
```

Expected output:

```text
[0.567, 0.767, 0.867]
```

## Test

```bash
python3 -m unittest tests/test_automate.py
```

## Why this is useful in enterprise data engineering
- Pattern maps to **feature engineering pipelines** before model training.
- Compose-style design is easy to migrate into Spark/Pandas UDF chains.
- Deterministic transforms are straightforward to version and audit.

## Uniqueness
- Minimal code, but clearly demonstrates composability and deterministic preprocessing—great as a rapid-prototype module you can extend into production-grade transformations.
