import streamlit as st
import importlib
from datetime import datetime

# -----------------------------
# Global App Configuration
# -----------------------------
st.set_page_config(
    page_title="Aadhaar Decision Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Page Registry (Single Source of Truth)
# -----------------------------
PAGES = {
    "System Health Overview": {
        "module": "views.SystemHealth",
        "title": "SYSTEM HEALTH OVERVIEW",
        "subtitle": "Real-time operational status and key metrics",
    },
    "Trends & Pattern Explorer": {
        "module": "views.TrendsExplorer",
        "title": "TRENDS & PATTERN EXPLORER",
        "subtitle": "Time-series analysis with region and time filters",
    },
    "Operational Stress & Anomalies": {
        "module": "views.StressAnomalies",
        "title": "OPERATIONAL STRESS & ANOMALIES",
        "subtitle": "Regional stress levels and anomaly detection",
    },
    "Priority & Risk Ranking": {
        "module": "views.PriorityRanking",
        "title": "PRIORITY & RISK RANKING",
        "subtitle": "Ranked list of regions by priority score with trend indicators",
    },
    "Recommendations & Explanation": {
        "module": "views.Recommendations",
        "title": "RECOMMENDATIONS & EXPLANATION",
        "subtitle": "Actionable recommendations with reasoning and confidence levels",
    },
}

# -----------------------------
# Sidebar (Fixed Product Surface)
# -----------------------------
with st.sidebar:
    st.markdown("### LOGO")
    st.markdown("**AADHAAR OPERATIONS**  \nAnalytics Dashboard")
    st.divider()

    selected_page = st.radio(
        "Navigation",
        list(PAGES.keys()),
        label_visibility="collapsed",
    )

    st.divider()
    st.caption("User: operations_officer")
    st.caption(f"Last Updated: {datetime.now().strftime('%d %b %Y')}")

# -----------------------------
# Page Header (Wireframe Style)
# -----------------------------
page_config = PAGES[selected_page]

st.markdown(f"## {page_config['title']}")
st.caption(page_config["subtitle"])
st.divider()

# -----------------------------
# Dynamic Page Rendering
# -----------------------------
try:
    page_module = importlib.import_module(page_config["module"])
    if hasattr(page_module, "render"):
        page_module.render()
    else:
        st.error("Page render() function not found.")
except Exception as e:
    st.error("Failed to load page.")
    st.exception(e)
