import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown("# 📦 Fulfillment Hub")

        st.caption(
            "XYZ Operations"
        )

        st.divider()

        st.markdown("### Today's operation")

        st.markdown("**200–300** orders/day")
        st.markdown("**1–2** office processors")
        st.markdown("**2–3** warehouse pickers")

        st.divider()

        st.markdown(
            """
            **Core workflow**

            Order  
            ↓  
            Picking  
            ↓  
            Packing  
            ↓  
            Staging  
            ↓  
            Courier pickup  
            ↓  
            Shipped
            """
        )

        st.divider()

        st.caption(
            "Demo data • Take-home prototype"
        )