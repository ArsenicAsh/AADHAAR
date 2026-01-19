import streamlit as st
import pandas as pd

DATA_PATH = "data/mock/priority_ranking.csv"

def render():
    # -----------------------------
    # Load Data
    # -----------------------------
    df = pd.read_csv(DATA_PATH)

    # =====================================================
    # SORT CONTROLS
    # =====================================================
    st.markdown("### SORT_CONTROLS")
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            sort_by = st.selectbox(
                "Sort By",
                ["Priority Score", "Impact Score"],
                index=0
            )

        with col2:
            risk_filter = st.multiselect(
                "Risk Level Filter",
                options=sorted(df["risk_level"].unique()),
                default=list(df["risk_level"].unique())
            )

        with col3:
            trend_filter = st.multiselect(
                "Trend Filter",
                options=sorted(df["trend"].unique()),
                default=list(df["trend"].unique())
            )

    st.divider()

    # =====================================================
    # APPLY FILTERS & SORT
    # =====================================================
    filtered_df = df[
        (df["risk_level"].isin(risk_filter)) &
        (df["trend"].isin(trend_filter))
    ]

    sort_column = "priority_score" if sort_by == "Priority Score" else "impact_score"
    filtered_df = filtered_df.sort_values(sort_column, ascending=False)

    # =====================================================
    # PRIORITY RANKING LIST
    # =====================================================
    st.markdown("### PRIORITY_RANKING_LIST")
    with st.container(border=True):
        for _, row in filtered_df.iterrows():
            col1, col2 = st.columns([1, 9])

            with col1:
                st.markdown(f"**#{int(row['rank'])}**")

            with col2:
                cols = st.columns(6)
                cols[0].write(row["region_id"])
                cols[1].write(row["region_name"])
                cols[2].write(f"{row['priority_score']:.1f}")
                cols[3].write(row["trend"])
                cols[4].write(row["risk_level"])
                cols[5].write(row["impact_score"])

            st.divider()

    # =====================================================
    # RISK DISTRIBUTION (FIXED)
    # =====================================================
    st.markdown("### RISK_DISTRIBUTION")
    with st.container(border=True):
        risk_counts = (
            df["risk_level"]
            .value_counts()
            .rename("Region Count")
        )

        st.bar_chart(risk_counts, use_container_width=True)
