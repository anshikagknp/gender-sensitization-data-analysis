"""
Gender Sensitization Survey — Streamlit Dashboard
Repo: anshikagknp/gender-sensitization-data-analysis

Reads data/synthetic_survey.csv (the seeded synthetic dataset already in the
repo) and turns it into an interactive dashboard with demographic filters
and six thematic views: Awareness, Stereotypes, Roles, Equality, GBV.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Gender Sensitization Survey — Kanpur Youth Study",
    page_icon="📊",
    layout="wide",
)

TEAL = "#0B5563"
CORAL = "#FF6F61"

# ---------------------------------------------------------------------------
# Theme CSS — makes the title, subtitle, info banner, and footer match the
# teal/coral palette used in the charts, instead of Streamlit's plain defaults
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
    .app-title {{
        font-size: 2.4rem;
        font-weight: 700;
        color: {TEAL};
        margin-bottom: 0.1rem;
    }}
    .app-subtitle {{
        font-size: 1rem;
        color: #4A4A4A;
        margin-bottom: 1rem;
    }}
    .app-banner {{
        background-color: #EAF3F3;
        border-left: 5px solid {TEAL};
        padding: 0.9rem 1.1rem;
        border-radius: 6px;
        font-size: 0.95rem;
        color: #1F1F1F;
        margin-bottom: 1.5rem;
    }}
    .app-footer {{
        text-align: center;
        color: #888888;
        font-size: 0.85rem;
        border-top: 1px solid #DDDDDD;
        padding-top: 0.8rem;
        margin-top: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/synthetic_survey.csv")


df = load_data()

# ---------------------------------------------------------------------------
# Question groupings, taken directly from the column names in
# data/synthetic_survey.csv
# ---------------------------------------------------------------------------
DIMENSIONS = {
    "Awareness": {
        "heard_term_gender_sensitization": "Heard the term \"gender sensitization\"",
        "gender_is_binary_or_nonbinary": "Views gender as binary or non-binary",
        "received_gender_training": "Received formal gender-sensitization training",
        "support_school_curriculum": "Supports adding it to school curriculum",
        "support_workplace_training": "Supports workplace training",
        "sensitization_helps_relationships": "Believes it helps relationships",
    },
    "Stereotypes & Roles": {
        "stereotype_men_rational_women_emotional": "\"Men are rational, women are emotional\"",
        "stereotype_women_bad_drivers": "\"Women are bad drivers\"",
        "view_okay_for_men_to_cry": "\"It's okay for men to cry\"",
        "stereotype_men_strong_women_weak": "\"Men are strong, women are weak\"",
        "stereotype_women_better_housekeepers": "\"Women are better housekeepers\"",
        "stereotype_gentle_men_less_masculine": "\"Gentle men are less masculine\"",
        "childcare_only_mother_responsibility": "Childcare is only the mother's job",
        "woman_home_man_provider_role": "Woman at home, man as provider",
        "chores_divided_equally_if_both_work": "Chores divided equally if both work",
    },
    "Equality & Workplace": {
        "support_equal_pay": "Supports equal pay for equal work",
        "support_gender_diversity_quotas": "Supports gender-diversity quotas",
        "discrimination_observed_nearby": "Has observed discrimination nearby",
        "support_gender_neutral_language": "Supports gender-neutral language",
        "encourage_girls_nontraditional_careers": "Encourages girls into non-traditional careers",
    },
    "Gender-Based Violence": {
        "man_should_have_final_say_home": "\"Man should have final say at home\"",
        "woman_should_not_tolerate_violence": "Woman should not tolerate violence",
        "sexist_jokes_okay": "Sexist jokes are okay",
        "sensitization_reduces_gbv": "Believes training reduces GBV",
    },
}

DEMOGRAPHIC_COLS = ["age_group", "gender", "education"]

# ---------------------------------------------------------------------------
# Sidebar — filters
# ---------------------------------------------------------------------------
st.sidebar.header("Filters")

age_filter = st.sidebar.multiselect(
    "Age group", sorted(df["age_group"].unique()), default=list(df["age_group"].unique())
)
gender_filter = st.sidebar.multiselect(
    "Gender", sorted(df["gender"].unique()), default=list(df["gender"].unique())
)
education_filter = st.sidebar.multiselect(
    "Education", sorted(df["education"].unique()), default=list(df["education"].unique())
)

filtered = df[
    df["age_group"].isin(age_filter)
    & df["gender"].isin(gender_filter)
    & df["education"].isin(education_filter)
]

st.sidebar.markdown(f"**{len(filtered)}** of **{len(df)}** respondents match your filters.")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-title">Gender Sensitization Data Analysis</div>',
    unsafe_allow_html=True,
)

if filtered.empty:
    st.error("No respondents match the current filters. Adjust the sidebar selections.")
    st.stop()

# ---------------------------------------------------------------------------
# Demographics overview
# ---------------------------------------------------------------------------
st.subheader("Respondent profile")
demo_cols = st.columns(len(DEMOGRAPHIC_COLS))
for col, field in zip(demo_cols, DEMOGRAPHIC_COLS):
    counts = filtered[field].value_counts(normalize=True).mul(100).round(1).reset_index()
    counts.columns = [field, "percentage"]
    fig = px.pie(
        counts,
        names=field,
        values="percentage",
        hole=0.5,
        title=field.replace("_", " ").title(),
        color_discrete_sequence=[TEAL, CORAL, "#8FB8B0", "#F2C078"],
    )
    fig.update_layout(showlegend=True, margin=dict(t=40, b=0, l=0, r=0), height=280)
    col.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------------------------------------------------
# Thematic tabs
# ---------------------------------------------------------------------------
st.subheader("Survey responses by theme")

tabs = st.tabs(list(DIMENSIONS.keys()))

for tab, dimension in zip(tabs, DIMENSIONS.keys()):
    with tab:
        questions = DIMENSIONS[dimension]

        # KPI row: show the top response share for each question
        kpi_cols = st.columns(len(questions))
        for kcol, (col_name, label) in zip(kpi_cols, questions.items()):
            top_value = filtered[col_name].value_counts(normalize=True).mul(100).round(0)
            top_label = top_value.index[0]
            top_pct = int(top_value.iloc[0])
            kcol.metric(label=label, value=f"{top_pct}%", delta=top_label, delta_color="off")

        # Detailed bar chart for a question picked from this theme
        st.write("")
        selected_question = st.selectbox(
            "Question detail",
            options=list(questions.keys()),
            format_func=lambda c: questions[c],
            key=f"select_{dimension}",
        )

        dist = (
            filtered[selected_question]
            .value_counts(normalize=True)
            .mul(100)
            .round(1)
            .reset_index()
        )
        dist.columns = ["response", "percentage"]

        fig = px.bar(
            dist.sort_values("percentage"),
            x="percentage",
            y="response",
            orientation="h",
            text="percentage",
            color_discrete_sequence=[TEAL],
        )
        fig.update_traces(texttemplate="%{text}%", textposition="outside")
        fig.update_layout(
            title=questions[selected_question],
            xaxis_title="% of respondents",
            yaxis_title="",
            height=350,
            margin=dict(t=60, b=20, l=0, r=20),
        )
        st.plotly_chart(fig, use_container_width=True)

st.markdown(
    '<div class="app-footer">Data: repo\'s seeded synthetic dataset · '
    'see README.md and docs/ for methodology and full findings.</div>',
    unsafe_allow_html=True,
)
