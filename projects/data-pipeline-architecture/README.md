# Data Pipeline Architecture

A minimal, end-to-end pipeline simulation implementing the core production pattern:

**ingest → transform → quality check → sink**

## Project layout

```text
data-pipeline-architecture/
├── pipeline.py
└── tests/
    └── test_pipeline.py
```

## Run

```bash
python3 pipeline.py
```

## Test

```bash
python3 -m unittest tests/test_pipeline.py
```

## What it demonstrates
- Domain event ingestion (`Event` dataclass).
- Currency normalization using FX mapping.
- Basic quality gate that blocks invalid rows.
- Sink step that aggregates and emits a load summary.

## Enterprise integration fit
- Ingestion can be replaced with Kafka/S3/CDC source connectors.
- Transform logic can be migrated to Spark/DBT models.
- Quality check step can be expanded to contract tests and threshold alerts.
- Sink can publish to Delta tables, Snowflake, BigQuery, or APIs.

## Uniqueness
- Clean architecture skeleton suitable for “productionizing” discussions (orchestration, idempotency, retries, and observability).
