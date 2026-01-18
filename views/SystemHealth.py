import streamlit as st

def render():
    """
    Renders the System Health Overview page.
    Assumes sidebar, title, and subtitle are already rendered by app.py
    """

    # =====================================================
    # HEADLINE SYSTEM STATUS
    # =====================================================
    st.markdown("### HEADLINE_SYSTEM_STATUS")
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**System Status**")
            st.caption("Overall operational state")
            st.write("Placeholder")

        with col2:
            st.markdown("**Active Regions**")
            st.caption("Regions currently operational")
            st.write("Placeholder")

        with col3:
            st.markdown("**Alert Level**")
            st.caption("Current system alert severity")
            st.write("Placeholder")

    st.divider()

    # =====================================================
    # KEY SUMMARY METRICS
    # =====================================================
    st.markdown("### KEY_SUMMARY_METRICS")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("**Total Enrollments**")
            st.caption("Cumulative count")
            st.write("Placeholder")

        with col2:
            st.markdown("**Daily Updates**")
            st.caption("Updates processed today")
            st.write("Placeholder")

        with col3:
            st.markdown("**Success Rate**")
            st.caption("Successful operations (%)")
            st.write("Placeholder")

        with col4:
            st.markdown("**Error Rate**")
            st.caption("Failed operations (%)")
            st.write("Placeholder")

    st.divider()

    # =====================================================
    # AFFECTED REGIONS BULLETIN
    # =====================================================
    st.markdown("### AFFECTED_REGIONS_BULLETIN")
    with st.container(border=True):
        for i in range(3):
            st.markdown(f"**Region {i + 1}**")
            st.caption("Issue summary and affected operations")
            st.write("Placeholder description of the issue impacting this region.")
            if i < 2:
                st.divider()
