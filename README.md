<p align="center">
  <h1 align="center">Perspectives on Gender Sensitization</h1>
  <p align="center">A Kanpur-Based Quantitative Study · Full Analytics Lifecycle</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen" alt="status"/>
  <img src="https://img.shields.io/badge/sample%20size-n%3D100-informational" alt="sample"/>
  <img src="https://img.shields.io/badge/synthetic%20dataset-1%2C000%20rows-blueviolet" alt="synthetic"/>
  <img src="https://img.shields.io/badge/Power%20BI-dashboard-F2C811?logo=powerbi&logoColor=black" alt="powerbi"/>
  <img src="https://img.shields.io/badge/Tableau-dashboard-E97627?logo=tableau&logoColor=white" alt="tableau"/>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="python"/>
  <img src="https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey" alt="license"/>
</p>

<p align="center">
  <a href="PROJECT_SHOWCASE.md">Portfolio Summary</a> ·
  <a href="dashboard_layout.md">Dashboard Spec</a> ·
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="#-quick-start">Quick Start</a>
</p>

---

## What this is

A quantitative social research project measuring gender sensitization awareness among 100 young respondents (18–35) in Kanpur, India — restructured here as a **end-to-end data analytics case study**. Covers survey design → primary data collection → frequency analysis → interactive BI dashboards → policy recommendations.

> **Original academic work:** MA Political Science dissertation, Christ Church College, Kanpur (CSJM University), 2023–24.  
> **Supervisor:** Vibha Dikshit, Associate Professor, Department of Political Science.

---

## Highlights

| | |
|---|---|
| 🎯 **70% sensitization rate** | ~70% of sampled Kanpur youth hold non-stereotypical gender attitudes |
| 🏛️ **60% training gap** | 60% have never received formal gender-sensitization training |
| 📊 **Two BI dashboards** | Power BI (7 pages) + Tableau (Overview + 6-point Story) |
| 🤖 **1,000-row synthetic dataset** | Statistically mirrors published findings; ML/demo-ready |
| 📐 **Star-schema data model** | Forward-compatible; drop-in ready for future row-level data |
| 🔬 **Six thematic dimensions** | Awareness · Stereotypes · Roles · Equality · GBV · Demographics |

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

**Headline result:** H1 (youth are fairly sensitized) and H2 (institutional training is missing) are both supported. The fastest policy lever is structured curriculum and workplace programs — not attitude campaigns.

---

## Dashboards

| | Power BI | Tableau |
|---|---|---|
| File | `dashboards/powerbi/*.pbix` | `dashboards/tableau/*.twbx` |
| Live link | *(add Publish-to-Web URL)* | *(add Tableau Public URL)* |
| Structure | Cover · Demographics · Awareness · Stereotypes · Roles · Equality · GBV · Insights | Overview + 6-point narrative Story |

Static exports: `dashboards/screenshots/` · Full design spec: [`dashboard_layout.md`](dashboard_layout.md)

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
| Visualization | Power BI · Tableau |
| Demographics | 86% aged 18–25 · 53% male / 47% female · 66% graduates |

*LGBTQIA+ respondents were not represented — acknowledged as a key limitation.*

---

## ⚡ Quick start

### Prerequisites
- Python ≥ 3.9
- Power BI Desktop or Tableau Desktop *(for dashboard files)*

### Installation

```bash
git clone https://github.com/anshikagknp/gender-sensitization-study.git
cd gender-sensitization-study

python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### Run notebooks *(v1.1 — coming soon)*

```bash
jupyter lab
# Open notebooks/ and run in order: 01 → 02 → 03
```

### Regenerate synthetic dataset

```bash
python data/synthetic/generate_dataset.py
# Outputs: data/synthetic/synthetic_survey.csv (seed=42, deterministic)
```

---

## Repository structure

```
gender-sensitization-study/
│
├── data/
│   ├── processed/              # Aggregate data model (from published %s)
│   └── synthetic/              # 1,000-row simulated dataset + generation script
│
├── dashboards/
│   ├── powerbi/                # .pbix + theme file
│   ├── tableau/                # .twbx + Story
│   └── screenshots/            # Static PNG exports
│
├── notebooks/                  # Jupyter analysis (v1.1+)
├── app/                        # Streamlit web app (v1.4+)
├── docs/                       # Questionnaire + design specs
├── report/                     # Full dissertation PDF
│
├── DATA.md                     # Data availability statement
├── DATA_GENERATION.md          # Synthetic data methodology & disclaimer
├── PROJECT_ARCHITECTURE.md     # Architecture + Mermaid data-flow diagram
├── PROJECT_SHOWCASE.md         # Recruiter-facing portfolio summary
├── ROADMAP.md                  # Planned features
├── CHANGELOG.md
├── CONTRIBUTING.md
├── requirements.txt
└── CITATION.cff
```

---

## Tech stack

<p>
  <img src="https://img.shields.io/badge/Google%20Forms-survey-7248B9?logo=googleforms&logoColor=white" alt="forms"/>
  <img src="https://img.shields.io/badge/Excel-analysis-217346?logo=microsoftexcel&logoColor=white" alt="excel"/>
  <img src="https://img.shields.io/badge/Power%20BI-dashboard-F2C811?logo=powerbi&logoColor=black" alt="powerbi"/>
  <img src="https://img.shields.io/badge/Tableau-dashboard-E97627?logo=tableau&logoColor=white" alt="tableau"/>
  <img src="https://img.shields.io/badge/Python-pandas%20%7C%20scikit--learn%20%7C%20plotly-3776AB?logo=python&logoColor=white" alt="python"/>
  <img src="https://img.shields.io/badge/Streamlit-web%20app%20(planned)-FF4B4B?logo=streamlit&logoColor=white" alt="streamlit"/>
</p>

---

## Ethical considerations

- All 100 responses were collected with informed consent via an anonymous Google Form. No PII was ever collected.
- The original response sheet has been permanently lost. Only published aggregate findings are represented here. See [`DATA.md`](DATA.md).
- The 1,000-row synthetic dataset is clearly labelled as simulated and must not be cited as primary research evidence. See [`DATA_GENERATION.md`](DATA_GENERATION.md).

---

## Citation

```bibtex
@misc{gupta2024gendersensitization,
  author    = {Gupta, Anshika},
  title     = {Perspectives on Gender Sensitization: A Kanpur-Based Comprehensive Study},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/anshikagknp/gender-sensitization-study}
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

---

## Author

**Anshika Gupta** — MA Political Science, Christ Church College, Kanpur (CSJM University)  
GitHub: [@anshikagknp](https://github.com/anshikagknp)  
*(Add LinkedIn / portfolio / email)*
