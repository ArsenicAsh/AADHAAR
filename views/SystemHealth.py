import streamlit as st
import pandas as pd


def render():
    # ===============================
    # Load mock data
    # ===============================
    summary_df = pd.read_csv("data/mock/system_health_summary.csv")
    metrics_df = pd.read_csv("data/mock/system_health_metrics.csv")
    affected_df = pd.read_csv("data/mock/affected_regions.csv")

    summary = summary_df.iloc[0]
    metrics = metrics_df.iloc[0]

    # ===============================
    # HEADLINE_SYSTEM_STATUS
    # ===============================
    st.markdown("### HEADLINE_SYSTEM_STATUS")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**System Status**")
        st.caption("Overall operational state")
        st.write(summary["system_status"])

    with col2:
        st.markdown("**Active Regions**")
        st.caption("Regions currently operational")
        st.write(int(summary["active_regions"]))

    with col3:
        st.markdown("**Alert Level**")
        st.caption("Current system alert severity")
        st.write(summary["alert_level"])

    st.divider()

    # ===============================
    # KEY_SUMMARY_METRICS
    # ===============================
    st.markdown("### KEY_SUMMARY_METRICS")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("**Total Enrollments**")
        st.caption("Cumulative count")
        st.write(f"{int(metrics['total_enrollments']):,}")

    with col2:
        st.markdown("**Daily Updates**")
        st.caption("Updates processed today")
        st.write(f"{int(metrics['daily_updates']):,}")

    with col3:
        st.markdown("**Success Rate (%)**")
        st.caption("Successful operations")
        st.write(metrics["success_rate"])

    with col4:
        st.markdown("**Error Rate (%)**")
        st.caption("Failed operations")
        st.write(metrics["error_rate"])

    st.divider()

    # ===============================
    # AFFECTED_REGIONS_BULLETIN
    # ===============================
    st.markdown("### AFFECTED_REGIONS_BULLETIN")

    if affected_df.empty:
        st.info("No affected regions detected.")
    else:
        for _, row in affected_df.iterrows():
            st.markdown(f"**{row['region_name']} ({row['region_id']})**")
            st.caption(f"Issue: {row['issue_type']} | Severity: {row['severity']}")
            st.write(f"Failed operations: {row['failed_ops']}")
            st.divider()
