# Stock Research AI Engine

A rule-based research assistant that scores microcap stocks and generates analyst-style theses.

## Core capabilities
- Multi-signal scoring: value, growth, leverage, momentum, insider buying.
- Score clamping to a 0..100 risk-controlled range.
- Ranked output for quick triage of opportunities.

## Project layout

```text
stock-research-ai-engine/
├── engine.py
├── sample_stocks.json
└── tests/
    └── test_engine.py
```

## Run

```bash
python3 engine.py --input sample_stocks.json --top 3
```

## Test

```bash
python3 -m unittest tests/test_engine.py
```

## Enterprise integration fit
- Works as a **research prioritization microservice** before deeper analyst workflows.
- Rules can be externalized into YAML/DB config for business-owned tuning.
- Output can be landed in a feature store or surfaced in investment operations dashboards.

## Uniqueness
- Deterministic “AI-style” thesis generation with transparent rule logic—helps communicate model explainability and governance readiness in interviews.
