# 📊 Dashboard Layout & BI Design Specification
### Gender Sensitization — Kanpur Youth Study (n = 100)

This document specifies the design of two parallel BI deliverables — a **Power BI** dashboard and a **Tableau** dashboard — built on the published, aggregated findings from the gender sensitization survey. It also defines the data model, wireframes, and interaction design so either dashboard can be reproduced today or extended once richer (respondent-level) data becomes available.

---

## 1. Data Foundations

### 1.1 Current data reality
The original respondent-level Google Form responses were lost (see `README.md` → Ethical Considerations). Only the **aggregated, already-published percentages** survive. The dashboards below are therefore designed as **aggregate insight dashboards** — KPI- and percentage-driven, not row-level drill dashboards — with a documented upgrade path (§1.3) for when the survey is re-run.

### 1.2 Reconstructed aggregate schema
Two flat tables, built directly from the README's published statistics, are sufficient to power both BI tools.

**`data/processed/survey_summary.csv`**

| dimension | question_id | question_text | response_label | percentage | favorable_flag |
|---|---|---|---|---|---|
| Awareness | AW01 | Heard the term "gender sensitization" | Yes | 77 | TRUE |
| Awareness | AW02 | Correctly defines gender as non-binary / social construct | Yes | 39 | TRUE |
| Awareness | AW03 | Received formal training on gender issues | No | 60 | FALSE |
| Stereotypes | ST01 | "It's okay for men to cry" | Agree | 82 | TRUE |
| Stereotypes | ST02 | "Men are strong, women are weak" | Disagree | 75 | TRUE |
| Stereotypes | ST03 | Holds ≥1 traditional competency stereotype | Yes | 40 | FALSE |
| Roles | RL01 | Childcare is exclusively mother's job | Disagree | 76 | TRUE |
| Roles | RL02 | Supports equal division of chores (dual-income) | Agree | 94 | TRUE |
| Equality | EQ01 | Supports equal pay for equal work | Agree | 91 | TRUE |
| Equality | EQ02 | Supports institutional gender-diversity policies | Agree | 70 | TRUE |
| Equality | EQ03 | Personally witnessed gender-based discrimination | Yes | 61 | FALSE |
| GBV | GB01 | Rejects "tolerate violence to keep family together" | Disagree | 70 | TRUE |
| GBV | GB02 | Opposes sexist jokes at others' expense | Agree | 77 | TRUE |
| GBV | GB03 | Believes training reduces GBV incidents | Agree | 63 | TRUE |

**`data/processed/demographics_summary.csv`**

| category | segment | percentage |
|---|---|---|
| Age Group | 18–25 | 86 |
| Age Group | 26–35 | 14 |
| Gender | Male | 53 |
| Gender | Female | 47 |
| Education | Graduate | 66 |
| Education | Postgraduate | 24 |
| Education | Other | 10 |

> Both CSVs live in `/data/processed/` and act as the single source of truth for both BI tools — keeping Power BI and Tableau outputs consistent with each other and with the README.

### 1.3 Future-state schema (recommended for the planned survey re-run)
A proper star schema, ready for the **Future Work → LGBTQIA+-inclusive stratified re-run**:

```
fact_responses          dim_respondent              dim_question
─────────────────       ─────────────────           ─────────────────
respondent_id (FK)      respondent_id (PK)           question_id (PK)
question_id (FK)        age_group                    dimension
response_value          gender_identity               question_text
response_date           education_level               question_type
                         region                        favorable_response
```

This enables true cross-filtering (e.g. "show Stereotypes answers filtered to Female, 18–25, Postgraduate") — not possible with aggregate-only data today. The dashboards below are deliberately laid out so this upgrade requires only a data-source swap, not a redesign.

---

## 2. Design Principles

| Element | Spec |
|---|---|
| Primary palette | Deep Teal `#0B5563`, Warm Coral `#FF6F61` (gap/concern highlight), Slate Gray `#4A4A4A` |
| Deliberately avoided | Pink/blue gender-binary color coding |
| Accessibility | WCAG-AA contrast minimum; colorblind-safe (checked against Deuteranopia/Protanopia); every chart has a data-label fallback so color is never the only signal |
| Typography | Headers: Segoe UI Semibold (Power BI) / Tableau Bold; Body: Segoe UI / Helvetica Neue |
| Grid | 12-column responsive grid, 16px gutter |
| KPI card style | Rounded 8px corners, value (32pt) + label (12pt) + micro-trend icon |
| Color logic | Favorable findings in Teal; awareness/training **gaps** in Coral — visually foregrounds the policy-intervention point |

---

## 3. Power BI Dashboard Design

### 3.1 File & workspace
`/dashboards/powerbi/GenderSensitization_Kanpur.pbix`

### 3.2 Data model
Flat model at the aggregate stage: `survey_summary` + `demographics_summary`, plus a disconnected `Dimension_Filter` table used purely as a slicer. No relational join is needed yet — both tables load independently and visuals bind directly to them, since there's no shared respondent key at the aggregate level (see §1.3 for the join-ready future schema).

### 3.3 Pages & navigation
| # | Page | Purpose |
|---|---|---|
| 1 | **Cover** | Title, one-line methodology, nav buttons, author credit |
| 2 | **Respondent Profile** | Demographics donuts + sample-size KPI |
| 3 | **Awareness & Knowledge** | 3 KPI cards + horizontal bar chart |
| 4 | **Stereotypes & Roles** | Diverging bar chart (agree vs. disagree) |
| 5 | **Equality & Workplace** | KPI cards + bar chart + discrimination-witnessed callout |
| 6 | **Gender-Based Violence** | Bar chart + training-impact indicator |
| 7 | **Insights & Recommendations** | Sensitization Index KPI, training-gap callout, recommendation text boxes |

Navigation: a persistent left-rail button bar (page navigation via bookmarks). Pages are thematically scoped, so cross-page slicer sync is intentionally off.

### 3.4 Visual inventory (sample — Page 3: Awareness & Knowledge)
| Visual | Type | Fields | Purpose |
|---|---|---|---|
| KPI Card | Card | `Heard Term %` (measure) | Headline awareness stat |
| KPI Card | Card | `Correct Definition %` | Conceptual-understanding gap |
| KPI Card | Card | `Training Gap %` | Training-gap headline, rendered in Coral |
| Bar chart | Clustered bar | `question_text`, `percentage` | Compare all three awareness statements |
| Donut | Donut chart | `Training Received` Yes/No | Proportion trained vs. untrained |

(Equivalent inventories apply to Pages 4–6, swapping in the relevant `dimension` filter.)

### 3.5 DAX measures
```dax
Heard Term % =
CALCULATE(
    SUM(survey_summary[percentage]),
    survey_summary[question_id] = "AW01"
)

Training Gap % =
CALCULATE(
    SUM(survey_summary[percentage]),
    survey_summary[question_id] = "AW03"
)

Sensitization Index =
AVERAGEX(
    FILTER(survey_summary, survey_summary[favorable_flag] = TRUE),
    survey_summary[percentage]
)

Favorable vs Gap Color =
IF(SELECTEDVALUE(survey_summary[favorable_flag]), "#0B5563", "#FF6F61")
```

### 3.6 Interactivity
- **Slicer:** `Dimension_Filter` (Awareness / Stereotypes / Roles / Equality / GBV) — drives Page 7 summary visuals.
- **Bookmark:** "Show Gaps Only" toggle that isolates `favorable_flag = FALSE` rows in Coral.
- **Tooltip page:** custom tooltip showing original question wording + sample-size note on hover.
- **Drill-through (future-state):** Page 7 → respondent-level detail page, once `fact_responses` exists (§1.3).

### 3.7 Theme (excerpt)
```json
{
  "name": "GenderSensitizationKanpur",
  "dataColors": ["#0B5563", "#FF6F61", "#4A4A4A", "#8FB8B0", "#F2C078"],
  "background": "#FFFFFF",
  "foreground": "#2A2A2A",
  "tableAccent": "#0B5563"
}
```

---

## 4. Tableau Dashboard Design

### 4.1 Workbook
`/dashboards/tableau/GenderSensitization_Kanpur.twbx`

### 4.2 Worksheets
| Sheet | Chart type | Source |
|---|---|---|
| `Demographics_Donut` | Pie / donut | demographics_summary |
| `Awareness_Bars` | Horizontal bar | survey_summary (dimension = Awareness) |
| `Stereotypes_Diverging` | Diverging bar | survey_summary (dimension = Stereotypes) |
| `Roles_Bars` | Bar | survey_summary (dimension = Roles) |
| `Equality_Bars` | Bar + 50% reference line | survey_summary (dimension = Equality) |
| `GBV_Bars` | Bar | survey_summary (dimension = GBV) |
| `Sensitization_Index_KPI` | Big-number indicator | calculated field |

### 4.3 Dashboard layout & actions
A single **"Overview" dashboard** (1366×768, fixed) arranges the sheets above in a 12-tile grid, plus:
- **Filter action:** clicking a `dimension` legend entry filters all bar-chart sheets to that theme.
- **Highlight action:** hovering a demographic donut segment highlights matching bars (future-state, once a respondent-level join key exists).
- **Parameter:** `Show Gaps Only` (Boolean) — recolors non-favorable rows Coral and grays out the rest.

### 4.4 Calculated fields
```
// Favorable-flag color
IF [favorable_flag] THEN "#0B5563" ELSE "#FF6F61" END

// Sensitization Index
{ FIXED : AVG(IF [favorable_flag] THEN [percentage] END) }

// Training Gap Index (applied to the AW03 row)
100 - [percentage]
```

### 4.5 Story (narrative flow)
A **Tableau Story** with six points mirrors the README's narrative arc — ideal for a portfolio walkthrough or a recruiter screen-share:
1. Who we surveyed (Demographics)
2. What they know (Awareness)
3. What they still believe (Stereotypes)
4. How they split household roles (Roles)
5. Where they stand on equality (Equality)
6. The policy ask: close the training gap (GBV + Recommendations)

### 4.6 Publishing
Publish to **Tableau Public** and link the embed URL from `README.md` and `PROJECT_SHOWCASE.md` — this turns a static repo into a live, clickable portfolio piece that doesn't require Tableau Desktop to view.

---

## 5. Wireframes

### 5.1 Home / Overview page
```
┌──────────────────────────────────────────────────────────────────────┐
│  GENDER SENSITIZATION — KANPUR YOUTH STUDY              n = 100        │
│  [Home] [Demographics] [Awareness] [Stereotypes] [Roles] [Equality]    │
│  [GBV] [Insights]                                                      │
├──────────────┬──────────────┬──────────────┬───────────────┬──────────┤
│  77%         │  60%         │  ~70%        │  Sensitization │  61%     │
│  Heard the   │  No Formal   │  Avg.        │  Index         │  Witness-│
│  Term        │  Training    │  Favorable   │  ~70%          │  ed Dis- │
│              │  (Coral)     │  Response    │                │  crimin. │
├──────────────┴──────────────┴──────────────┴────────────────┴──────────┤
│   [Radar chart: avg. favorable % per thematic dimension]               │
│        Awareness ●───● Equality                                        │
│       Stereotypes ●  ⬡  ● Roles                                        │
│              GBV  ●───●                                                │
├──────────────────────────────────────┬──────────────────────────────────┤
│  Demographics donuts ×3 (Age /        │  Text box: headline insight +    │
│  Gender / Education)                  │  policy recommendation           │
└──────────────────────────────────────┴──────────────────────────────────┘
```

### 5.2 Thematic detail page (example: Awareness & Knowledge)
```
┌──────────────────────────────────────────────────────────────────────┐
│  ◀ Back to Overview            AWARENESS & KNOWLEDGE                   │
├───────────────┬───────────────┬────────────────────────────────────────┤
│  77%          │  39%          │  60%                                    │
│  Heard Term   │  Correct Def. │  No Formal Training         (Coral)     │
├───────────────┴───────────────┴────────────────────────────────────────┤
│  Heard the term            ████████████████████████████████░░  77%     │
│  Correct definition        ███████████████░░░░░░░░░░░░░░░░░░░  39%     │
│  Received training         ████████████████░░░░░░░░░░░░░░░░░░  40%     │
├───────────────────────────────────────┬──────────────────────────────────┤
│  Donut: Trained (40%) vs Untrained    │  Note: "Training is the single   │
│  (60%)                                 │  largest lever for improving     │
│                                         │  sensitization."                 │
└───────────────────────────────────────┴──────────────────────────────────┘
```

### 5.3 Mobile / responsive note
Both tools: KPI cards stack 2-per-row → 1-per-row below 768px; top nav collapses into a hamburger / page-dropdown; bar charts switch to vertical scroll instead of horizontal pagination.

---

## 6. Folder & file naming convention
```
dashboards/
├── powerbi/
│   ├── GenderSensitization_Kanpur.pbix
│   └── theme/GenderSensitizationKanpur.json
├── tableau/
│   ├── GenderSensitization_Kanpur.twbx
│   └── story/GenderSensitization_Story.twbx
└── screenshots/
    ├── overview.png
    ├── awareness.png
    ├── stereotypes.png
    ├── roles.png
    ├── equality.png
    └── gbv.png
```

## 7. Build checklist
- [ ] Load `survey_summary.csv` + `demographics_summary.csv` into both tools
- [ ] Apply the theme palette (§2) consistently across both tools
- [ ] Build Power BI pages 1–7 with the DAX measures in §3.5
- [ ] Build Tableau worksheets + Overview dashboard + Story (§4.2–4.5)
- [ ] Export six PNG screenshots → `/dashboards/screenshots/`
- [ ] Publish the Tableau workbook to Tableau Public; embed link in README
- [ ] Export the Power BI dashboard to PDF as a no-login fallback for recruiters
- [ ] Cross-check both tools render identical headline numbers (77 / 39 / 60 / 70 / 91 / 61 / etc.)
