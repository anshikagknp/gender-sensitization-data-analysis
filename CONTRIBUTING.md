# Contributing

Thank you for considering a contribution to this project. Contributions that improve reproducibility, documentation, visualisation quality, or analytical tooling are warmly welcome.

---

## What this repository accepts

| ✅ Welcome | ❌ Out of scope |
|---|---|
| Bug fixes in analysis notebooks or scripts | Changes to published research findings or statistics |
| New visualisation notebooks | New primary data collection under this project name |
| Streamlit / web app improvements | Modifications to `synthetic_survey.csv` without updating `DATA_GENERATION.md` |
| Documentation improvements | Removal of ethical disclosures or data-availability statements |
| Performance improvements (pandas, plotting) | Breaking changes to the data model without a migration path |
| Accessibility improvements (charts, dashboards) | |
| Additional ML/statistical notebooks | |

---

## Getting started

### 1. Fork and clone

```bash
git clone https://github.com/<your-username>/gender-sensitization-study.git
cd gender-sensitization-study
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

### 3. Create a branch

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bug-description
```

---

## Branch naming

| Prefix | When to use |
|---|---|
| `feat/` | New feature or notebook |
| `fix/` | Bug fix |
| `docs/` | Documentation only |
| `refactor/` | Code restructure, no behaviour change |
| `chore/` | Dependency updates, tooling |

---

## Commit style

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add chi-square significance testing notebook
fix: correct percentage rounding in awareness chart
docs: clarify synthetic data limitations in DATA_GENERATION.md
chore: upgrade pandas to 2.2.0
```

---

## Pull request checklist

Before opening a PR, confirm the following:

- [ ] Code runs without errors from a clean install (`pip install -r requirements.txt`)
- [ ] Notebooks have been re-run top-to-bottom and outputs are committed
- [ ] No raw respondent data has been introduced
- [ ] `DATA_GENERATION.md` updated if `synthetic_survey.csv` is changed
- [ ] Docstrings / comments explain the logic
- [ ] PR description explains *what* changed and *why*

---

## Reporting issues

Open a GitHub Issue and include:

- A clear title
- Steps to reproduce (for bugs)
- Expected vs. actual behaviour
- Environment details (OS, Python version, package versions)

---

## Code style

- **Python:** [PEP 8](https://peps.python.org/pep-0008/); format with `black`, lint with `flake8`
- **Notebooks:** clear markdown headers, one logical section per cell group
- **Markdown:** sentence case for headings; ATX-style (`#`) headers only

---

## Licensing

By contributing, you agree that your contributions will be licensed under the same terms as this repository:
- Documentation, findings, and write-ups: **CC BY-NC 4.0**
- Code and scripts: **MIT License**

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold it.
