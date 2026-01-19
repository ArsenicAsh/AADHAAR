import streamlit as st
import pandas as pd

DATA_PATH = "data/mock/recommendations.csv"

def render():
    """
    Renders the Recommendations & Explanation page.
    """

    # -----------------------------
    # Load & Sanitize Data
    # -----------------------------
    df = pd.read_csv(DATA_PATH)

    # 🔒 HARD TYPE FIXES (THIS SOLVES YOUR ERROR)
    df["confidence"] = pd.to_numeric(df["confidence"], errors="coerce")
    df["severity"] = df["severity"].astype(str)
    df["responsible_level"] = df["responsible_level"].astype(str)
    df["status"] = df["status"].astype(str)

    # Drop any broken rows (safety)
    df = df.dropna(subset=["confidence"])

    # -----------------------------
    # FILTER CONTROLS
    # -----------------------------
    st.markdown("### FILTER_CONTROLS")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            severity_filter = st.multiselect(
                "Severity",
                options=sorted(df["severity"].unique()),
                default=list(df["severity"].unique())
            )

        with col2:
            responsible_filter = st.multiselect(
                "Responsible Level",
                options=sorted(df["responsible_level"].unique()),
                default=list(df["responsible_level"].unique())
            )

        with col3:
            confidence_threshold = st.slider(
                "Minimum Confidence",
                min_value=0.0,
                max_value=1.0,
                value=0.7,
                step=0.05
            )

        with col4:
            status_filter = st.multiselect(
                "Status",
                options=sorted(df["status"].unique()),
                default=list(df["status"].unique())
            )

    st.divider()

    # -----------------------------
    # APPLY FILTERS
    # -----------------------------
    filtered_df = df[
        (df["severity"].isin(severity_filter)) &
        (df["responsible_level"].isin(responsible_filter)) &
        (df["confidence"] >= confidence_threshold) &
        (df["status"].isin(status_filter))
    ]

    # -----------------------------
    # RECOMMENDATIONS LIST
    # -----------------------------
    st.markdown("### RECOMMENDATIONS_LIST")

    if filtered_df.empty:
        st.info("No recommendations match the selected filters.")
        return

    for _, row in filtered_df.iterrows():
        with st.container(border=True):

            header_cols = st.columns([6, 2, 2])
            with header_cols[0]:
                st.markdown(f"**{row['action_title']}**")
                st.caption(f"Recommendation ID: {row['recommendation_id']}")

            with header_cols[1]:
                st.metric("Severity", row["severity"])

            with header_cols[2]:
                st.metric("Confidence", f"{row['confidence']:.2f}")

            st.markdown("**Recommended Action**")
            st.write(row["recommended_action"])

            st.markdown("**Reason**")
            st.write(row["reason"])

            meta_cols = st.columns(4)
            meta_cols[0].write(f"**Region:** {row['region_name']} ({row['region_id']})")
            meta_cols[1].write(f"**Responsible Level:** {row['responsible_level']}")
            meta_cols[2].write(f"**Estimated Impact:** {row['estimated_impact']}")
            meta_cols[3].write(f"**Timeline:** {row['timeline']}")

            st.caption(f"Status: {row['status']}")

    # -----------------------------
    # MODEL EXPLANATION
    # -----------------------------
    st.divider()
    st.markdown("### MODEL_EXPLANATION")
    with st.container(border=True):
        st.markdown("""
        **Model Version:** v1.0 (Rule-based Decision Intelligence)

        **Confidence Methodology**
        - Based on anomaly severity, recurrence frequency, and impact score
        - Normalized between 0 and 1 for interpretability
        - Used to prioritize actions under constrained resources

        This layer transforms analytics into **decision-ready intelligence**.
        """)
