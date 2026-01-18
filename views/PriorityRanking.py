import streamlit as st

def render():
    """
    Renders the Priority & Risk Ranking page.
    Assumes sidebar and page header are handled by app.py
    """

    # =====================================================
    # SORT CONTROLS
    # =====================================================
    st.markdown("### SORT_CONTROLS")
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Sort By**")
            st.write("Placeholder")

        with col2:
            st.markdown("**Risk Level Filter**")
            st.write("Placeholder")

        with col3:
            st.markdown("**Time Range**")
            st.write("Placeholder")

    st.divider()

    # =====================================================
    # PRIORITY RANKING LIST
    # =====================================================
    st.markdown("### PRIORITY_RANKING_LIST")
    with st.container(border=True):
        for rank in range(1, 9):
            col1, col2 = st.columns([1, 9])

            with col1:
                st.markdown(f"**#{rank}**")

            with col2:
                row_cols = st.columns(6)
                row_cols[0].write("Region ID")
                row_cols[1].write("Region Name")
                row_cols[2].write("Priority Score")
                row_cols[3].write("Trend")
                row_cols[4].write("Risk Level")
                row_cols[5].write("Impact Score")

            if rank < 8:
                st.divider()

    st.divider()

    # =====================================================
    # RISK DISTRIBUTION
    # =====================================================
    st.markdown("### RISK_DISTRIBUTION")
    with st.container(border=True):
        st.write("Bar chart placeholder")
        st.write("risk_level vs region_count")
