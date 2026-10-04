import streamlit as st


def page_header(title, subtitle):

    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">FULFILLMENT HUB</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )