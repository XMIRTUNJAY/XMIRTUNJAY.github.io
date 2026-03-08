# AI Microcap Research Engine

Interview-ready, runnable project that mimics a buy-side research workflow for microcap screening.

## What this project demonstrates
- Data engineering basics: structured input ingestion (`universe` + `sentiment`) and output artifact generation.
- Quant-style scoring model using weighted factors (valuation, growth, quality, momentum, sentiment, risk).
- Clear explainability through generated investment thesis + factor-level contribution summary.
- Reproducible CLI pipeline that outputs a Markdown report for sharing with stakeholders.

## Architecture

```text
Universe JSON + Sentiment JSON
          │
          ▼
 Factor Engineering (valuation/growth/quality/momentum/risk/sentiment)
          │
          ▼
  Conviction Scoring + Banding (High Conviction / Watchlist / Speculative)
          │
          ▼
 Ranked Picks + Thesis Generation
          │
          ▼
 output/report.md
```

## Project structure

```text
ai-microcap-research-engine/
├── data/
│   ├── microcap_universe.json
│   └── news_sentiment.json
├── output/
├── tests/
│   └── test_engine.py
├── main.py
└── README.md
```

## Run

```bash
cd projects/ai-microcap-research-engine
python3 main.py --top 3
```

Custom output path:

```bash
python3 main.py --top 4 --output output/interview_report.md
```

## Test

```bash
cd projects/ai-microcap-research-engine
python3 -m unittest tests/test_engine.py
```

## Interview talking points
- Why factor weights are set this way and how you would calibrate them with historical backtests.
- How to productionize: orchestrate daily runs, source market/news APIs, persist to lakehouse, expose via dashboard.
- Risk controls: add liquidity filters, sector constraints, and confidence intervals for score stability.
