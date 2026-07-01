# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Streamlit web app for interactive dashboard exploration
- Chi-square significance testing across demographic subgroups
- Python/pandas analysis notebook reproducing all frequency distributions
- ML classification notebook (attitude prediction) using `synthetic_survey.csv`
- Tableau Public embed link
- Power BI Publish-to-Web embed link

---

## [1.0.0] — 2024-01-01

### Added
- `synthetic_survey.csv` — 1,000-row synthetic respondent dataset (25 columns) generated to statistically mirror published aggregate findings; seeded with `random.seed(42)` for reproducibility
- `DATA_GENERATION.md` — full transparency document: generation methodology, appropriate/inappropriate uses, and explicit disclaimer that the data is 100% synthetic
- `DATA.md` — data availability statement explaining why original row-level data cannot be shared (respondent confidentiality, Google Form loss, no separate backup)
- `PROJECT_SHOWCASE.md` — recruiter-facing two-minute portfolio summary with skills-to-role mapping table
- `README.md` — full project documentation covering methodology, findings, dashboards, ethics, and future work
- `dashboard_layout.md` — complete Power BI and Tableau design specification (data model, DAX/calculated fields, color system, wireframes)
- `docs/questionnaire.md` — reconstructed survey instrument inferred from dissertation charts
- `data/processed/survey_summary.csv` — aggregate findings data model (reconstructed from published percentages)
- `data/processed/demographics_summary.csv` — demographic breakdown aggregate table
- `CITATION.cff` — machine-readable citation metadata
- `CONTRIBUTING.md` — contribution guidelines
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `SECURITY.md` — security policy
- `ROADMAP.md` — planned enhancements
- `requirements.txt` — pinned Python dependencies
- `.gitignore` — Python + Jupyter + VS Code + macOS + Windows rules
- `LICENSE` — CC BY-NC 4.0 (documentation/findings) + MIT (code)

### Research findings (original dissertation — 2023-24)
- n=100 respondents, ages 18–35, Kanpur, India
- 77% awareness of the term "Gender Sensitization"
- ~70% average favorable ("sensitized") response rate across six thematic dimensions
- ~60% institutional training gap (never received formal gender training)
- H1 and H2 both supported by frequency-distribution analysis

[Unreleased]: https://github.com/anshikagknp/gender-sensitization-study/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/anshikagknp/gender-sensitization-study/releases/tag/v1.0.0
