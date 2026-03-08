# Automated Financial Analysis

A CLI utility that converts raw financial statement rows into analyst-friendly KPI metrics.

## Metrics computed
- Gross margin
- Operating margin
- Net margin
- Free cash flow margin
- Debt / EBITDA leverage proxy

## Project layout

```text
automated-financial-analysis/
├── analyze.py
├── sample_financials.csv
└── tests/
    └── test_analyze.py
```

## Run

```bash
python3 analyze.py --input sample_financials.csv
```

## Test

```bash
python3 -m unittest tests/test_analyze.py
```

## Enterprise integration fit
- Can be used as a **metrics standardization step** in finance data marts.
- Fits in scheduled batch jobs to enrich earnings datasets before BI publishing.
- Easy to map output into warehouse tables (`company`, `period`, `metric_name`, `metric_value`).

## Uniqueness
- Fast, deterministic KPI extraction with no heavy dependencies—ideal as an interview demo for building explainable financial transformation logic quickly.
