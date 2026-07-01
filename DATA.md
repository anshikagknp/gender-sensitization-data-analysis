# Data Availability Statement

## Status

This repository contains **summaries and a reconstructed questionnaire** derived from the dissertation *Perspectives on Gender Sensitization: A Kanpur-based Comprehensive Study* (Anshika Gupta, 2023–24). It does **not** include the underlying raw survey responses or a downloadable respondent-level dataset.

## Why the Original Survey Data Cannot Be Shared

The dissertation reports only **aggregated, percentage-level results**, presented as pie charts in Chapter 4. No row-level/individual response data was ever published as part of the work, and none is available to redistribute here, for three specific reasons:

1. **Respondent confidentiality.** The survey asked about sensitive personal attitudes — including views on domestic violence, household authority, and personal experience of discrimination. With a sample of only 100 people, and several demographic fields (age band, gender, education) attached to each response, row-level data could plausibly be re-identified even without names attached. Withholding individual-level responses protects respondents who answered in confidence.
2. **The original Google Form is lost.** The form and its linked response sheet were hosted on Google Forms as part of the 2023–24 academic project. That form and the raw response sheet are no longer accessible, so even an anonymized export can't currently be recovered or checked against the published charts.
3. **No separate archived dataset exists.** Only the chart-level summaries that made it into the dissertation (Chapter 4) survive — there is no separate backup file (CSV/XLSX) of the original 100 responses.

## What This Repository Provides Instead

- `key_findings.md` — the published aggregate results (percentages and response counts) exactly as reported in the dissertation.
- `questionnaire.md` — a reconstruction of the survey instrument, inferred from chart titles and legends, for transparency about what was actually asked.

## Future Plans: Synthetic Data

To let this repository support reproducible analysis, charting, or tooling demos without compromising anyone's privacy, a future addition will include a **synthetic dataset** — simulated, individual-level responses generated to statistically match the published aggregates (e.g., the 77%/23% awareness split, the 53%/47% gender split).

That synthetic dataset will:
- Be clearly labelled as **simulated, not real respondent data**.
- Approximate the published distributions, without attempting to recover or infer any actual respondent's real answers.
- Be intended for illustrative, educational, and methodological use (e.g., testing analysis scripts or dashboards) — not as a substitute for genuine primary research.

Until that synthetic dataset is added, treat any analysis beyond what's in `key_findings.md` as unavailable for this study.

---
*Derived from: Perspectives on Gender Sensitization: A Kanpur-based Comprehensive Study (Anshika Gupta, Christ Church College, Kanpur, 2023–24).*
