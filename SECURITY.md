# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ Yes |

---

## Reporting a vulnerability

If you discover a security vulnerability in this repository's code, scripts, or dependencies, please **do not open a public GitHub Issue**.

Report it privately:

1. Open a [GitHub Security Advisory](https://github.com/anshikagknp/gender-sensitization-study/security/advisories/new) (preferred).
2. Or email the maintainer directly (see the repository's About section for contact details).

You can expect an acknowledgement within **72 hours** and a resolution plan within **7 days**.

---

## Data security notes

This repository does **not** contain any real respondent-level data.

- The original 100 survey responses were collected via an anonymous Google Form and have since been permanently lost (see `DATA.md`).
- The included `synthetic_survey.csv` is 100% simulated data generated from published aggregate percentages. It contains no PII and poses no re-identification risk (see `DATA_GENERATION.md`).
- **Do not commit** any file containing real survey responses, names, email addresses, or any personally identifiable information to this repository. The `.gitignore` is configured to block `data/raw/` and common accidental-commit patterns.

---

## Dependency vulnerabilities

If you identify a vulnerable dependency in `requirements.txt`, please open a standard GitHub Issue or submit a pull request with the updated version pin.
