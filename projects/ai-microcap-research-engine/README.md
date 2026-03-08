# AI Microcap Research Engine

Interview-ready research workflow that merges structured fundamentals with sentiment signals and produces a ranked markdown report.

## What it demonstrates
- Structured ingestion (`universe` + `sentiment`) and artifact generation.
- Weighted factor model (valuation, growth, quality, momentum, sentiment, risk penalty).
- Explainability: factor contribution transparency + generated thesis.
- Repeatable CLI execution suitable for scheduling.

## Architecture

```text
Universe JSON + Sentiment JSON
          │
          ▼
Factor Engineering
(valuation/growth/quality/momentum/sentiment/risk)
          │
          ▼
Conviction Scoring + Banding
(High Conviction / Watchlist / Speculative)
          │
          ▼
Ranked Picks + Thesis Generation
          │
          ▼
output/report.md
```

## Project layout

```text
ai-microcap-research-engine/
├── data/
│   ├── microcap_universe.json
│   └── news_sentiment.json
├── output/
│   └── report.md
├── tests/
│   └── test_engine.py
├── main.py
└── README.md
```

## Run

```bash
python3 main.py --top 3
```

Custom output path:

```bash
python3 main.py --top 4 --output output/interview_report.md
```

## Test

```bash
python3 -m unittest tests/test_engine.py
```

## Enterprise integration fit
- Replace JSON with market data APIs and NLP sentiment streams.
- Schedule as daily batch scoring in Airflow/Prefect.
- Persist results to warehouse/lakehouse tables for BI and downstream consumption.
- Add data quality checks, model versioning, and drift monitoring.

## Uniqueness
- Combines quant-like factor ranking and narrative report generation in one deterministic package, making it strong for “business impact + engineering depth” storytelling.
