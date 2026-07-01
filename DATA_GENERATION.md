# DATA_GENERATION.md

## ⚠️ This dataset is 100% synthetic

`synthetic_survey.csv` does **not** contain any real participant responses.
No individual-level data from the original dissertation, *"Perspectives on
Gender Sensitization: A Kanpur-based comprehensive study"* (Anshika Gupta,
Christ Church College, Kanpur, 2023–24), was ever available to this script —
that study only published **aggregate percentages** (e.g., "77% of
respondents had heard of the term Gender Sensitization") derived from its
own 100 real survey participants. Those original individual responses were
never accessed, reconstructed, or reproduced here in any form.

This synthetic dataset exists **purely for analytics, dashboarding, and
machine-learning demonstration purposes** — for example, practicing data
cleaning, building visualizations, or testing classification/clustering
pipelines on survey-shaped categorical data.

## What was generated

- **1000 synthetic respondents**, each with a randomly generated ID
  (`R0001`–`R1000`).
- **25 columns** covering demographics (age group, gender, education) and
  attitudinal questions spanning gender sensitization awareness, gender
  stereotypes, gender roles, gender equality, and gender-based violence —
  mirroring the *topics* covered in Chapter 4 of the dissertation.

## How values were generated

1. **Baseline probabilities** for each categorical response were set to
   approximately match the percentages reported in the dissertation (e.g.,
   "82% agreed it is okay for men to cry" → roughly 82% probability of
   `Agree` in the synthetic data, before added variation).
2. **Random sampling with noise**: each of the 1000 synthetic respondents'
   answers was drawn independently using Python's `random` module from
   these probability distributions, so the resulting dataset reproduces the
   published aggregates only *approximately* (typically within a few
   percentage points), exactly as you'd expect from natural sampling
   variation — not as an exact replica.
3. **Invented relationships between variables** were deliberately added so
   the dataset is useful for demonstrating correlation/regression/ML
   techniques. For example:
   - Respondents with higher education levels were given a slightly higher
     probability of reporting awareness of the term "Gender Sensitization."
   - Older respondents were given a slightly higher probability of having
     received formal gender-related training.
   - Respondents who had never heard the term, or never received training,
     were given a modestly higher probability of agreeing with traditional
     gender stereotypes.

   **These relationships are entirely fictional constructs introduced by
   the generation script.** The original dissertation reports only
   univariate percentages and does **not** claim, test, or demonstrate any
   such cross-variable relationships. Do not cite this dataset, or any
   pattern found within it, as evidence of real-world relationships between
   education, age, training, and attitudes.

## Files in this package

| File | Purpose |
|---|---|
| `generate_dataset.py` | The Python script that produces `synthetic_survey.csv` from scratch using only random sampling. Re-running it (with the fixed random seed `42`) reproduces the same dataset. |
| `synthetic_survey.csv` | The 1000-row synthetic dataset itself. |
| `DATA_GENERATION.md` | This document. |

## Appropriate uses

- Practicing pandas/SQL data wrangling
- Building example dashboards or charts
- Testing ML classification/clustering code on realistic categorical data
- Teaching demonstrations about survey data structure

## Inappropriate uses

- Citing this file as real survey evidence in academic papers, news
  articles, or policy briefs
- Treating any statistic, correlation, or trend in this file as a finding
  about actual attitudes in Kanpur or elsewhere
- Substituting this file for the original dissertation's findings

If you need the **real, published** aggregate findings, refer directly to
Chapter 4 of the original dissertation.
