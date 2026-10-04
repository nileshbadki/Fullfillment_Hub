import pandas as pd
import streamlit as st

from components.header import page_header


page_header(
    "Picking",
    "Give warehouse workers a simple list of "
    "what needs to be picked next."
)


data = st.session_state.data

orders = data["orders"]


picking = orders[
    orders.status == "Picking"
].copy()


new_priority = orders[
    (
        orders.status == "New"
    )
    &
    (
        orders.priority == "Priority"
    )
].copy()


if not new_priority.empty:

    picking = pd.concat(
            [
                picking,
                new_priority
            ],
            ignore_index=True
        )
    


st.markdown(
    "### Orders ready for picking"
)


if picking.empty:

    st.success(
        "No orders currently waiting for picking."
    )

else:

    for _, order in picking.iterrows():

        priority_text = (
            "🔴 PRIORITY"
            if order.priority == "Priority"
            else "Standard"
        )

        with st.container(border=True):

            st.markdown(
                f"### {order.order_id} · {priority_text}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Product:** "
                    f"{order.product_name}"
                )

                st.write(
                    f"**Variant:** "
                    f"{order.variant}"
                )

                st.write(
                    f"**Quantity:** "
                    f"{order.quantity}"
                )

            with col2:

                st.write(
                    f"**Pick location:** "
                    f"{order.pick_location}"
                )

                st.write(
                    f"**Warehouse:** "
                    f"{order.warehouse}"
                )

                st.write(
                    f"**Deadline:** "
                    f"{order.pickup_deadline}"
                )


            if st.button(
                "Confirm Pick",
                key=f"pick_{order.order_id}"
            ):

                orders.loc[
                    orders.order_id ==
                    order.order_id,
                    "status"
                ] = "Packing"

                st.success(
                    f"{order.order_id} picked."
                )

                st.rerun()