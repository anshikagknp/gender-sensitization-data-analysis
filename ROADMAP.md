# Roadmap

This document tracks planned improvements to the repository. Items are loosely ordered by priority. Contributions toward any of these are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## v1.1 — Analysis notebooks

**Goal:** make all frequency-distribution analysis fully reproducible in Python.

- [ ] `notebooks/01_eda.ipynb` — exploratory data analysis on `synthetic_survey.csv`: distributions, missing-value audit, demographic crosstabs
- [ ] `notebooks/02_frequency_analysis.ipynb` — reproduce all six thematic frequency tables from the dissertation (Awareness → GBV) using pandas
- [ ] `notebooks/03_visualisations.ipynb` — publication-ready charts (seaborn / plotly) matching the dissertation's pie / bar charts
- [ ] Add `make notebook` / `make analysis` targets to a `Makefile` for one-command reproducibility

---

## v1.2 — Statistical depth

**Goal:** move beyond descriptive percentages to inferential statistics.

- [ ] Chi-square tests across demographic subgroups (age × awareness, gender × stereotype attitudes, education × training receipt)
- [ ] Cramér's V effect-size reporting alongside chi-square p-values
- [ ] Confidence intervals on key percentages (awareness, training gap, favorable-response rate)
- [ ] `notebooks/04_statistical_tests.ipynb`

---

## v1.3 — Machine learning

**Goal:** demonstrate ML workflows on realistic survey-shaped categorical data.

- [ ] Feature engineering: encode Likert / categorical responses to numeric
- [ ] Binary classification: predict "sensitized vs. not" (favorable composite score ≥ threshold)
- [ ] Models: Logistic Regression baseline → Random Forest → XGBoost; SHAP feature importance
- [ ] Clustering: K-Modes / K-Prototypes to identify respondent attitude clusters
- [ ] `notebooks/05_ml_classification.ipynb`, `notebooks/06_clustering.ipynb`
- [ ] MLflow or similar for experiment tracking (optional)

---

## v1.4 — Streamlit web app

**Goal:** interactive, browser-based version of the dashboards; no BI tool required.

- [ ] `app/` directory with a multi-page Streamlit app
- [ ] Pages: Overview · Demographics · Awareness · Stereotypes · Roles · Equality · GBV · Insights
- [ ] Filters: age group, gender, education level
- [ ] KPI cards, bar/pie charts (Plotly), data table with download button
- [ ] Deployed to Streamlit Community Cloud with a public URL
- [ ] `README.md` badge linking to the live app

---

## v1.5 — Interactive survey

**Goal:** allow future researchers to re-run a version of this survey and feed responses into the same pipeline.

- [ ] Streamlit-based web form mirroring the original questionnaire structure
- [ ] Responses stored in a local SQLite or PostgreSQL database
- [ ] Live dashboard auto-updates as new responses are submitted
- [ ] Data-governance guard: anonymisation applied before any storage; no PII collected

---

## v1.6 — Dashboard publishing

**Goal:** make BI dashboards viewable without installing Power BI or Tableau Desktop.

- [ ] Power BI: Publish-to-Web embed link added to README and `PROJECT_SHOWCASE.md`
- [ ] Tableau: Tableau Public upload; embed link added to README
- [ ] Static PNG / GIF exports for quick preview in README (already partially done)
- [ ] Dashboard screenshots refreshed to match v1.0 design spec

---

## v2.0 — Extended study

**Goal:** address key limitations of the original n=100 study.

- [ ] Re-run the survey with a larger, stratified sample inclusive of LGBTQIA+ respondents
- [ ] Expand geographic scope for cross-city comparison (Lucknow, Delhi, Mumbai)
- [ ] Add qualitative layer: semi-structured interviews / focus groups for attitudinal "why"
- [ ] Longitudinal component: re-survey the same cohort after an institutional training intervention
- [ ] Publish a technical research paper alongside the updated data

---

## Stretch goals

- [ ] REST API exposing aggregate statistics as JSON (FastAPI)
- [ ] GitHub Actions CI: lint notebooks, run analysis, publish updated charts on every push to `main`
- [ ] Docker container for fully portable, one-command environment setup
- [ ] Multilingual documentation (Hindi)

---

*Want to contribute to any of these? Open an issue or see [CONTRIBUTING.md](CONTRIBUTING.md).*
