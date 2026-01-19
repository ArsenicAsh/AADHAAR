import streamlit as st
import pandas as pd

DATA_PATH = "data/mock/"

def render():
    st.markdown("## OPERATIONAL STRESS & ANOMALIES")
    st.caption("Regional stress levels and anomaly detection")

    # =====================================================
    # Load Data
    # =====================================================
    stress_overview = pd.read_csv(f"{DATA_PATH}stress_overview.csv")
    region_stress = pd.read_csv(f"{DATA_PATH}region_stress.csv")
    anomaly_events = pd.read_csv(f"{DATA_PATH}anomaly_events.csv")

    st.divider()

    # =====================================================
    # STRESS LEVEL OVERVIEW
    # =====================================================
    st.markdown("### STRESS_LEVEL_OVERVIEW")
    with st.container(border=True):
        cols = st.columns(3)

        for idx, level in enumerate(["High", "Medium", "Low"]):
            value = stress_overview.loc[
                stress_overview["stress_level"] == level, "region_count"
            ].values[0]

            with cols[idx]:
                st.markdown(f"**{level} Stress**")
                st.caption(f"Regions under {level.lower()} stress")
                st.markdown(f"### {value}")

    st.divider()

    # =====================================================
    # REGION STRESS CARDS
    # =====================================================
    st.markdown("### REGION_STRESS_CARDS")

    for _, row in region_stress.iterrows():
        with st.container(border=True):
            st.markdown(f"**{row['region_name']} ({row['region_id']})**")
            st.write(f"**Stress Level:** {row['stress_level']}")
            st.write(f"**Anomaly Type:** {row['anomaly_type']}")
            st.write(f"**Affected Operations:** {row['affected_ops']}")
            st.write(f"**Duration:** {row['duration_hours']} hours")

    st.divider()

    # =====================================================
    # ANOMALY DETAILS TABLE
    # =====================================================
    st.markdown("### ANOMALY_DETAILS_TABLE")

    display_df = anomaly_events.copy()
    display_df["timestamp"] = pd.to_datetime(display_df["timestamp"])

    st.dataframe(
        display_df.sort_values("timestamp", ascending=False),
        use_container_width=True,
        hide_index=True,
    )
