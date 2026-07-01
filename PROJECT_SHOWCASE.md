# 🏆 Project Showcase: Gender Sensitization — Kanpur Youth Study
### A full-cycle data analytics case study — from survey design to interactive BI dashboards

---

## 30-Second Pitch
A self-designed, self-run quantitative survey (n=100) measuring how gender-sensitized Kanpur's 18–35 youth actually are — turned into a complete analytics deliverable: rigorous methodology, frequency analysis across six thematic dimensions, and interactive Power BI + Tableau dashboards built for a non-technical, policy-facing audience.

## At a Glance
| Metric | Value |
|---|---|
| Respondents | 100 |
| Sampling | Convenience + gender-stratified |
| Thematic dimensions analyzed | 6 |
| Avg. favorable ("sensitized") response rate | ~70% |
| Institutional training gap | ~60% never formally trained |
| Dashboards delivered | Power BI + Tableau |
| Literature sources synthesized | 30+ |

## The Problem
Gender sensitization is widely discussed in Indian policy circles but rarely *measured* at the city level. Without a baseline, schools and employers can't tell whether awareness campaigns are working or where to intervene. This project builds that baseline for Kanpur.

## The Approach
1. **Design** — built a closed-ended questionnaire from a 30+ source literature review, structured around six thematic dimensions (Demographics, Awareness, Stereotypes, Roles, Equality, GBV).
2. **Collect** — distributed via Google Forms using convenience + gender-stratified sampling; 100 clean responses.
3. **Analyze** — frequency-distribution and percentage analysis per dimension; two hypotheses tested.
4. **Visualize** — translated raw percentages into a BI-ready data model and two parallel dashboards (see [`dashboard_layout.md`](dashboard_layout.md)).
5. **Recommend** — converted findings into a concrete, policy-relevant call to action.

## Key Findings
- 🟢 **Attitudes are ahead of institutions.** ~70% of respondents hold favorable, non-stereotypical attitudes — but 60% have never received formal gender training.
- 🟢 **Toxic-masculinity rejection is strong:** 82% agree it's okay for men to cry; 75% reject "men are strong, women are weak."
- 🟡 **Conceptual understanding lags behind awareness:** 77% have heard the term "gender sensitization," but only 39% can correctly define gender as a social construct — a knowledge-vs-vocabulary gap.
- 🔴 **The real lever is institutional, not attitudinal:** the data supports H1 (youth are fairly sensitized) and H2 (training infrastructure is missing) — meaning the fastest ROI for policymakers is structured curriculum/workplace programs, not attitude campaigns.

## Dashboards
Two BI dashboards make these findings explorable rather than static:
- **Power BI** — 7-page dashboard (Cover → Insights), KPI-driven, themed with an accessible, non-gender-coded color system.
- **Tableau** — Overview dashboard plus a 6-point narrative Story, ideal for a guided walkthrough.

Full design spec (data model, DAX/calculated fields, color system, wireframes): [`dashboard_layout.md`](dashboard_layout.md).

## Skills → Role Mapping
| Skill demonstrated in this project | Data Analyst | Data Scientist | BI / Analytics Engineer | AI/ML Engineer |
|---|:---:|:---:|:---:|:---:|
| Survey design & sampling theory | ✅ | ✅ | | |
| Hypothesis formulation & testing | ✅ | ✅ | | |
| Frequency-distribution / descriptive statistics | ✅ | ✅ | | |
| Star-schema data modeling | | | ✅ | ✅ |
| DAX / Tableau calculated fields | | | ✅ | |
| Dashboard UX & accessible color design | ✅ | | ✅ | |
| Data governance, ethics & confidentiality | ✅ | ✅ | ✅ | ✅ |
| Translating analysis into stakeholder recommendations | ✅ | ✅ | ✅ | |
| Literature synthesis → feature/question design | | ✅ | | ✅ |

## Engineering Around a Real-World Constraint
Midway through this project's repository migration, the original respondent-level spreadsheet was permanently lost. Rather than reconstruct or fabricate row-level data, this project instead:
- Documented the loss transparently in the README rather than hiding it,
- Rebuilt an **aggregate-only data model** (§1.2 of `dashboard_layout.md`) sufficient to power both dashboards without compromising the (already-anonymous) original respondents,
- Designed a **forward-compatible star schema** so a future re-run can drop in respondent-level data with zero dashboard redesign.

This mirrors a constraint analysts hit constantly — working with partial, governed, or access-restricted data — and shows the engineering response to it, not just the happy path.

## Tech Stack
Google Forms · Excel · Power BI · Tableau · Markdown
*(Python/pandas recommended for the next iteration — see Future Work below.)*

## Limitations & Future Roadmap
- LGBTQIA+ respondents were not represented in this sample — flagged as a limitation, not an oversight.
- Next iteration: stratified sample inclusive of LGBTQIA+ respondents; mixed-methods (interviews) to capture the *why*; chi-square testing across subgroups; cross-city comparison beyond Kanpur.

## Explore This Repository
- 📄 Full write-up: [`report/full-dissertation.pdf`](report/full-dissertation.pdf)
- 📊 Dashboard design spec: [`dashboard_layout.md`](dashboard_layout.md)
- 📋 Survey instrument: [`docs/questionnaire.md`](docs/questionnaire.md)
- 📈 Charts: [`visuals/charts/`](visuals/charts/)
- 📘 Full README: [`README.md`](README.md)

## About the Author
**Anshika Gupta** — MA Political Science (Christ Church College, Kanpur — CSJM University).
*(Add LinkedIn / email / portfolio link here.)*
