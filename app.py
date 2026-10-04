import streamlit as st
from utils.data_loader import load_data

st.set_page_config(
    page_title="Fulfillment Hub",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    border-right: 1px solid #29324a;
}

.hero {
    padding: 8px 0 25px 0;
}

.eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    opacity: .55;
}

.hero h1 {
    font-size: 34px;
    margin: 5px 0;
}

.hero p {
    opacity: .65;
}

.metric-card {
    border: 1px solid #29324a;
    border-radius: 14px;
    padding: 18px;
    min-height: 120px;
    background: #121a2d;
}

.metric-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: .5px;
    opacity: .6;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.metric-note {
    font-size: 12px;
    opacity: .55;
    margin-top: 5px;
}

.alert-card {
    border: 1px solid #54333b;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
    background: #21171c;
}

.info-card {
    border: 1px solid #29324a;
    border-radius: 12px;
    padding: 15px;
    background: #121a2d;
    margin-bottom: 12px;
}

.priority-text {
    font-weight: 800;
}

.small-muted {
    font-size: 12px;
    opacity: .55;
}
</style>
""", unsafe_allow_html=True)


if "data" not in st.session_state:
    st.session_state.data = load_data()


st.title("📦 Fulfillment Hub")

st.caption(
    "A simple operations control center for XYZ's "
    "e-commerce fulfillment workflow."
)

st.info(
    "Use the navigation on the left to manage today's orders, "
    "picking, packing, staging, inventory and exceptions."
)