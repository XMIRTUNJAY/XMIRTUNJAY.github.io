# Equity Research Dashboard

A lightweight static dashboard for presenting valuation and growth snapshots in a browser-friendly format.

## Project layout

```text
equity-research-dashboard/
├── index.html
└── README.md
```

## Run

Open `index.html` in any browser.

Optional local server:

```bash
python3 -m http.server 8080
# then open http://localhost:8080/projects/equity-research-dashboard/
```

## Enterprise integration fit
- Can serve as a quick **presentation layer prototype** before moving to React/BI tooling.
- Easy to connect to REST endpoints or generated JSON artifacts from upstream pipelines.
- Useful for executive summaries of factor signals, KPI trends, and risk flags.

## Uniqueness
- Fastest possible dashboard bootstrap for stakeholder demos; great for proving workflow value before investing in heavier front-end frameworks.
