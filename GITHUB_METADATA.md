# GitHub Metadata Reference

Use the content below when configuring the repository on GitHub.com.

---

## 11 · GitHub Topics (15 optimized)

Paste these into **Settings → Topics**:

```
gender-sensitization
social-research
quantitative-research
survey-analysis
data-analytics
power-bi
tableau
synthetic-data
scikit-learn
pandas
streamlit
india
kanpur
open-data
data-science
```

---

## 12 · Repository Description (≤ 350 characters)

```
Quantitative study of gender sensitization attitudes among Kanpur youth (n=100) — full analytics lifecycle: survey design, frequency analysis, Power BI & Tableau dashboards, 1,000-row synthetic dataset, and ML-ready pipeline. MA Political Science · CSJM University · 2023-24.
```
*(271 characters)*

---

## 13 · Release Notes — v1.0.0

**Title:** `v1.0.0 — Initial public release`

```markdown
## What's included

This is the first public release of the Gender Sensitization Study repository.

### Research
- Frequency-distribution analysis across 6 thematic dimensions (Awareness, Stereotypes, Roles, Equality, GBV, Demographics) based on n=100 primary survey responses collected in Kanpur, 2023–24
- Two hypotheses tested and supported: H1 (youth are fairly gender-sensitized, ~70%) and H2 (institutional training gap exists, ~60%)

### Data
- `data/processed/survey_summary.csv` — aggregate findings table reconstructed from published dissertation percentages
- `data/synthetic/synthetic_survey.csv` — 1,000-row synthetic respondent dataset (25 columns) generated to statistically mirror published aggregates; seeded at `42` for full reproducibility
- `DATA.md` — data availability statement
- `DATA_GENERATION.md` — full synthetic-data methodology and disclaimer

### Dashboards
- Power BI: 7-page dashboard (Cover → Insights), KPI-driven, star-schema data model
- Tableau: Overview dashboard + 6-point narrative Story
- Full design spec in `dashboard_layout.md`

### Repository infrastructure
- `requirements.txt`, `.gitignore`, `CITATION.cff`
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- `CHANGELOG.md`, `ROADMAP.md`, `PROJECT_ARCHITECTURE.md`

### What's coming
See [ROADMAP.md](ROADMAP.md) — next milestone is Jupyter analysis notebooks (v1.1) and chi-square testing (v1.2).
```

---

## 14 · GitHub About Section

```
Quantitative gender sensitization study · n=100 · Kanpur · Power BI + Tableau dashboards · synthetic ML dataset · full analytics lifecycle
```

---

## 15 · Repository Badges (Shields.io)

Copy the full block into the top of `README.md` (already included — provided here separately for reference):

```markdown
![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Sample Size](https://img.shields.io/badge/sample%20size-n%3D100-informational)
![Synthetic Dataset](https://img.shields.io/badge/synthetic%20dataset-1%2C000%20rows-blueviolet)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626?logo=jupyter&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-dashboard-F2C811?logo=powerbi&logoColor=black)
![Tableau](https://img.shields.io/badge/Tableau-dashboard-E97627?logo=tableau&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-planned-FF4B4B?logo=streamlit&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikitlearn&logoColor=white)
![License CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)
![License MIT](https://img.shields.io/badge/code%20license-MIT-green)
![GitHub last commit](https://img.shields.io/github/last-commit/anshikagknp/gender-sensitization-study)
![GitHub stars](https://img.shields.io/github/stars/anshikagknp/gender-sensitization-study?style=social)
```
