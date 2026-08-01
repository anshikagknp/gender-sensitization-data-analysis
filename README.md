<h1 align="center">Survey Analysis: Perspectives on Gender Sensitization</h1>
<p align="center"><a href="https://gender-sensitization-data-analysis.streamlit.app/">
  <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App"/>
</a></p>

<p align="center">
  <a href="docs/executive_summary.md">Executive Summary</a> ·
  <a href="docs/dashboard_spec.md">Dashboard Spec</a> ·
  <a href="docs/architecture.md">Architecture</a> 
</p>

---

## Highlights

| | |
|---|---|
| **70% sensitization rate** | ~70% of sampled Kanpur youth hold non-stereotypical gender attitudes |
| **60% training gap** | 60% have never received formal gender-sensitization training |
| **33 visualizations** | Chart-by-chart breakdown of every survey question plus thematic infographics |
| **1,000-row synthetic dataset** | Statistically mirrors published findings; reproducible via a seeded generator script |
| **Three-notebook pipeline** | Data cleaning → EDA → statistical analysis, in order |
| **Six thematic dimensions** | Awareness · Stereotypes · Roles · Equality · GBV · Demographics |

---

## What is this?

An **end-to-end data analytics case study** that covers survey design → primary data collection → cleaning → exploratory and statistical analysis → visualization → key findings, built on a 100-respondent gender-sensitization survey from Kanpur, India (18–35 age group). Originally conducted as part of an MA Political Science thesis; restructured here into a full Python-based analytics pipeline and portfolio project.

📄 **[Read the full paper](https://anshikagknp.github.io/gender-sensitization-data-analysis/research-paper.html)**

---

## Screenshots

<img width="1470" height="802" alt="image" src="https://github.com/user-attachments/assets/9c0d5098-3232-40e8-a22d-7ba931b77331" />

<img width="1466" height="802" alt="image" src="https://github.com/user-attachments/assets/cc168aa1-ce3a-47c7-9ddf-bfd5f1c860cc" />

---

## Key findings

**Awareness**
- 77% had heard the term "gender sensitization" — but only ~39% could correctly define gender as a social construct (knowledge–vocabulary gap)
- 60% had never received any formal gender training

**Stereotypes & Roles**
- 82% agreed it is acceptable for men to cry — strong rejection of toxic-masculinity norms
- 75% disagreed that "men are strong, women are weak"
- 94% supported equal division of household chores when both partners work

**Equality & GBV**
- 91% supported equal pay for equal work
- 70% rejected the idea that women should tolerate violence to preserve a family
- 63% believed gender-sensitization training reduces incidents of gender-based violence

**Headline result:** youth are fairly sensitized, but institutional training is largely missing. The fastest policy lever is structured curriculum and workplace programs — not attitude campaigns.

Full write-up: [`docs/key_findings.md`](docs/key_findings.md) · [`docs/executive_summary.md`](docs/executive_summary.md)

---

## Methodology

| Component | Detail |
|---|---|
| Research type | Quantitative · descriptive |
| Instrument | Closed-ended Google Form |
| Sample size | 100 respondents |
| Sampling | Convenience + gender-stratified |
| Target population | Youth aged 18–35, Kanpur |
| Analysis | Frequency distribution · percentage analysis |
| Demographics | 86% aged 18–25 · 53% male / 47% female · 66% graduates |

*LGBTQIA+ respondents were not represented — acknowledged as a key limitation.*

Full details: [`docs/methodology.md`](docs/methodology.md) · Survey instrument: [`docs/questionnaire.md`](docs/questionnaire.md)

---

## Repository structure

```
gender-sensitization-survey-analysis/
│
├── data/
│   ├── generate_dataset.py     # Synthetic data generator (seeded, deterministic)
│   └── synthetic_survey.csv    # 1,000-row simulated dataset
│
├── analysis/
│   ├── Data_Cleaning.ipynb
│   ├── EDA.ipynb
│   └── Statistical_Analysis.ipynb
│
├── visualizations/             # 33 chart & infographic PNGs
│
├── docs/
│   ├── methodology.md
│   ├── questionnaire.md
│   ├── key_findings.md
│   ├── executive_summary.md
│   ├── architecture.md         # Project architecture & data flow
│   ├── dashboard_spec.md       # Dashboard design spec
│   └── research_paper_portfolio.pdf
│
├── requirements.txt
├── CITATION.cff
└── LICENSE
```

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Notebook Environment | Jupyter Notebook |
| Web App / Dashboard | Streamlit |
| Data Collection | Google Forms |
| Version Control | Git & GitHub |

---

## Ethical considerations

- All 100 responses were collected with informed consent via an anonymous Google Form. No Personally Identifiable Information was ever collected.
- The original response sheet has not been used due to confidentiality clause. Only published aggregate findings are represented here.
- The 1,000-row synthetic dataset is clearly labelled as simulated and must not be cited as primary research evidence.

---

## Citation

```bibtex
@misc{gupta2024gendersensitization,
  author    = {Gupta, Anshika},
  title     = {Perspectives on Gender Sensitization: A Kanpur-Based Quantitative Study},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/anshikagknp/gender-sensitization-survey-analysis}
}
```

See [`CITATION.cff`](CITATION.cff) for the full machine-readable citation.

---

## Acknowledgements

- **Supervisor:** Vibha Dikshit, Associate Professor, Department of Political Science, Christ Church College, Kanpur
- Original literature review drew on 30+ academic sources on gender sensitization policy in India

---

## License

| Content | License |
|---|---|
| Findings, documentation, write-up | [CC BY-NC 4.0](LICENSE) |
| Code and scripts | MIT |
| GitHub | [@anshikagknp](https://github.com/anshikagknp) |
