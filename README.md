# Premium Portfolio — Mirtunjay Kumar

A premium creative-style personal portfolio for GitHub Pages, designed with a minimal, cinematic aesthetic inspired by high-end photographer/model portfolios.

## Stack
- HTML5
- TailwindCSS (CDN)
- Custom CSS3
- Vanilla JavaScript

## Project structure

```text
.
├── index.html
├── styles.css
├── script.js
├── assets/
│   ├── images/
│   └── icons/
├── sections/
│   ├── hero.html
│   ├── about.html
│   ├── projects.html
│   ├── experience.html
│   └── contact.html
└── projects/
    ├── ai-microcap-research-engine/
    ├── analytics-automation/
    ├── automated-financial-analysis/
    ├── data-pipeline-architecture/
    ├── equity-research-dashboard/
    └── stock-research-ai-engine/
```

## Included sections
- Hero (full-screen, animated visual treatment)
- About
- Project portfolio gallery
- Featured project spotlight
- Experience timeline
- Skills visualization
- Ideas/Blog cards
- Contact

## Run locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy to GitHub Pages
1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose:
   - **Source:** Deploy from a branch
   - **Branch:** `main` (or your default branch), `/ (root)`
4. Save and wait for GitHub Pages to publish.
5. Site URL will be available as:
   - `https://<your-username>.github.io/<repo-name>/`
   - If this repo is named `<your-username>.github.io`, URL is `https://<your-username>.github.io/`.

## Optional custom domain
1. Add a `CNAME` file in repo root with your domain.
2. In **Settings → Pages**, set the custom domain.
3. Update your DNS:
   - `A` records to GitHub Pages IPs, or
   - `CNAME` to `<your-username>.github.io` for subdomains.
4. Enable HTTPS in GitHub Pages settings.

## Notes
- Designed to stay lightweight and fast.
- Uses lazy-loading for images.
- Includes dark/light mode toggle and smooth reveal animations.
