# Mirtunjay Kumar Portfolio + Data Engineering Project Pack

This repository is both:
- a GitHub Pages portfolio site, and
- a **plug-and-play mini project suite** for showcasing production-style data engineering and analytics capabilities in interviews.

## Repository map (what is where)

```text
.
├── index.html / styles.css / script.js      # Portfolio UI shell
├── sections/                                # Portfolio page sections
└── projects/
    ├── ai-microcap-research-engine/         # Factor + sentiment ranking engine
    ├── analytics-automation/                # Functional transformation pipeline
    ├── automated-financial-analysis/        # CSV financial KPI analyzer
    ├── data-pipeline-architecture/          # Ingest→transform→quality→sink simulation
    ├── equity-research-dashboard/           # Static dashboard frontend
    └── stock-research-ai-engine/            # Rule-based stock scoring assistant
```

## Why this is strong for interviews

Each project demonstrates a reusable engineering pattern that can be integrated into enterprise stacks:
- **Deterministic pipelines** with clear input/output contracts.
- **Configurable scoring logic** that can be externalized to metadata/config files.
- **Testable modules** with unit-level validation.
- **Operationalization readiness** (batch schedules, quality gates, and report artifacts).

## Quick validation commands

```bash
python3 projects/analytics-automation/automate.py
python3 projects/automated-financial-analysis/analyze.py --input projects/automated-financial-analysis/sample_financials.csv
python3 projects/data-pipeline-architecture/pipeline.py
python3 projects/stock-research-ai-engine/engine.py --input projects/stock-research-ai-engine/sample_stocks.json --top 3
python3 projects/ai-microcap-research-engine/main.py --top 3

python3 -m unittest projects/analytics-automation/tests/test_automate.py
python3 -m unittest projects/automated-financial-analysis/tests/test_analyze.py
python3 -m unittest projects/data-pipeline-architecture/tests/test_pipeline.py
python3 -m unittest projects/stock-research-ai-engine/tests/test_engine.py
python3 -m unittest projects/ai-microcap-research-engine/tests/test_engine.py
```

## Enterprise integration strategy

Use these projects as modular building blocks:
1. **Ingestion layer**: Replace local JSON/CSV with APIs, Kafka, or object storage landing zones.
2. **Transformation layer**: Containerize Python modules and run via Airflow/Prefect/Databricks Jobs.
3. **Quality & governance**: Add schema validation (Pandera/Great Expectations) and lineage tracking.
4. **Serving layer**: Publish outputs to warehouse tables, BI dashboards, or internal REST endpoints.
5. **Monitoring layer**: Add logging, SLAs, and anomaly alerts.

This gives you a credible “I can deliver value in 30-60 days” narrative: ship pilot modules fast, then harden them for enterprise controls.
