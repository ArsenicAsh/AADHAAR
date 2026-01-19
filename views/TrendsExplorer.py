import streamlit as st
import pandas as pd
from pathlib import Path


def render():
    """
    Renders the Trends & Pattern Explorer page.
    Uses mock time-series data from data/mock/trends_timeseries.csv
    """

    # =====================================================
    # LOAD MOCK DATA
    # =====================================================
    DATA_PATH = Path("data/mock/trends_timeseries.csv")

    df = pd.read_csv(DATA_PATH, parse_dates=["date"])

    # =====================================================
    # FILTER CONTROLS
    # =====================================================
    st.markdown("### FILTER_CONTROLS")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            regions = sorted(df["region_name"].unique())
            selected_regions = st.multiselect(
                "Region Filter",
                regions,
                default=regions,
            )

        with col2:
            start_date = st.date_input(
                "Start Time Period",
                df["date"].min(),
            )

        with col3:
            end_date = st.date_input(
                "End Time Period",
                df["date"].max(),
            )

        with col4:
            metric_type = st.selectbox(
                "Metric Type",
                ["Enrollments", "Updates"],
            )

    # =====================================================
    # FILTER DATA
    # =====================================================
    filtered_df = df[
        (df["region_name"].isin(selected_regions))
        & (df["date"] >= pd.to_datetime(start_date))
        & (df["date"] <= pd.to_datetime(end_date))
    ]

    st.divider()

    # =====================================================
    # ENROLLMENTS TIME SERIES
    # =====================================================
    st.markdown("### ENROLLMENTS_TIME_SERIES")
    with st.container(border=True):
        if filtered_df.empty:
            st.warning("No data available for selected filters.")
        else:
            enrollment_ts = filtered_df.pivot(
                index="date",
                columns="region_name",
                values="enrollments",
            )
            st.line_chart(enrollment_ts)

    st.divider()

    # =====================================================
    # UPDATES TIME SERIES
    # =====================================================
    st.markdown("### UPDATES_TIME_SERIES")
    with st.container(border=True):
        if filtered_df.empty:
            st.warning("No data available for selected filters.")
        else:
            updates_ts = filtered_df.pivot(
                index="date",
                columns="region_name",
                values="updates",
            )
            st.line_chart(updates_ts)

    st.divider()

    # =====================================================
    # PATTERN SUMMARY (Simple Derived Insights)
    # =====================================================
    st.markdown("### PATTERN_SUMMARY")
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)

        if filtered_df.empty:
            col1.write("—")
            col2.write("—")
            col3.write("—")
        else:
            total_enrollments = (
                filtered_df.groupby("date")["enrollments"].sum()
            )

            trend_direction = (
                "Increasing"
                if total_enrollments.iloc[-1] > total_enrollments.iloc[0]
                else "Decreasing"
            )

            peak_date = total_enrollments.idxmax().strftime("%d %b %Y")
            variance_level = (
                "High"
                if total_enrollments.std() > total_enrollments.mean() * 0.1
                else "Low"
            )

            with col1:
                st.markdown("**Trend Direction**")
                st.write(trend_direction)

            with col2:
                st.markdown("**Peak Period**")
                st.write(peak_date)

            with col3:
                st.markdown("**Variance Level**")
                st.write(variance_level)
