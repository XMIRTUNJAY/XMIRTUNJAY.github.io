# Mirtunjay Kumar Portfolio

A premium, creative-style developer portfolio designed for GitHub Pages.

## Tech Stack
- HTML5
- TailwindCSS (CDN)
- Custom CSS3
- Vanilla JavaScript

## Included Projects (implemented)
- `projects/stock-research-ai-engine` — AI-style stock signal scoring CLI
- `projects/automated-financial-analysis` — financial ratio automation from CSV
- `projects/equity-research-dashboard` — browser-based valuation snapshot dashboard
- `projects/data-pipeline-architecture` — ingest/transform/quality/sink pipeline simulator
- `projects/analytics-automation` — functional analytics transformation pipeline

## Structure

```text
.
├── index.html
├── styles.css
├── script.js
├── projects/
│   ├── stock-research-ai-engine/
│   ├── automated-financial-analysis/
│   ├── equity-research-dashboard/
│   ├── data-pipeline-architecture/
│   └── analytics-automation/
├── assets/
│   ├── images/
│   └── icons/
└── sections/
    ├── hero.html
    ├── about.html
    ├── projects.html
    ├── experience.html
    └── contact.html
```

## Local Preview
Open `index.html` in a browser.

## Deploy to GitHub Pages
1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose:
   - Source: **Deploy from a branch**
   - Branch: **main** (or your default branch)
   - Folder: **/ (root)**
4. Save and wait for GitHub to publish.
5. Your site will be available at:
   `https://<your-username>.github.io/<repo-name>/`

## Optional Custom Domain
1. Add your domain in **Settings → Pages → Custom domain**.
2. Add a `CNAME` file in repo root with your domain.
3. Configure DNS records from your domain provider to GitHub Pages.
