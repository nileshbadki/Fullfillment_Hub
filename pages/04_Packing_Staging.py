import streamlit as st

from components.header import page_header


page_header(
    "Packing & Staging",
    "Verify packed orders and keep courier-ready "
    "packages visible until pickup."
)


data = st.session_state.data

orders = data["orders"]
shipments = data["shipments"]


st.markdown("## 📦 Packing verification")


packing = orders[
    orders.status == "Packing"
]


if packing.empty:

    st.info(
        "No orders waiting for packing."
    )

else:

    for _, order in packing.iterrows():

        with st.container(border=True):

            st.markdown(
                f"### {order.order_id}"
            )

            st.write(
                f"**Product:** "
                f"{order.product_name}"
            )

            st.write(
                f"**Expected variant:** "
                f"{order.variant}"
            )

            st.write(
                f"**Quantity:** "
                f"{order.quantity}"
            )

            st.write(
                f"**Shipping method:** "
                f"{order.shipping_method}"
            )


            product_ok = st.checkbox(
                "Product verified",
                key=f"product_{order.order_id}"
            )

            variant_ok = st.checkbox(
                "Variant verified",
                key=f"variant_{order.order_id}"
            )

            quantity_ok = st.checkbox(
                "Quantity verified",
                key=f"quantity_{order.order_id}"
            )

            label_ok = st.checkbox(
                "Shipping label attached",
                key=f"label_{order.order_id}"
            )


            if st.button(
                "Confirm Packing",
                key=f"pack_{order.order_id}"
            ):

                if all(
                    [
                        product_ok,
                        variant_ok,
                        quantity_ok,
                        label_ok
                    ]
                ):

                    orders.loc[
                        orders.order_id ==
                        order.order_id,
                        "status"
                    ] = "Packed"

                    st.success(
                        f"{order.order_id} packed successfully."
                    )

                    st.rerun()

                else:

                    st.error(
                        "Complete all verification "
                        "checks before packing."
                    )


st.markdown("## 🚚 Staging")


staged = orders[
    orders.status.isin(
        [
            "Packed",
            "Staged",
            "Pickup Missed"
        ]
    )
]


if staged.empty:

    st.info(
        "No packages currently in staging."
    )

else:

    st.dataframe(
        staged[
            [
                "order_id",
                "customer_name",
                "priority",
                "status",
                "shipping_method",
                "pickup_deadline",
                "staging_location"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


st.markdown("## Courier pickup")


for _, order in staged.iterrows():

    with st.container(border=True):

        st.markdown(
            f"### {order.order_id}"
        )

        st.write(
            f"Courier: **{order.shipping_method}**"
        )

        st.write(
            f"Pickup: **{order.pickup_deadline}**"
        )

        st.write(
            f"Staging location: "
            f"**{order.staging_location}**"
        )

        col1, col2 = st.columns(2)

        with col1:

            if order.status in [
                "Packed",
                "Pickup Missed"
            ]:

                if st.button(
                    "Mark Ready",
                    key=f"stage_{order.order_id}"
                ):

                    orders.loc[
                        orders.order_id ==
                        order.order_id,
                        "status"
                    ] = "Staged"

                    st.rerun()


        with col2:

            if order.status == "Staged":

                if st.button(
                    "Mark Shipped",
                    key=f"ship_{order.order_id}"
                ):

                    orders.loc[
                        orders.order_id ==
                        order.order_id,
                        "status"
                    ] = "Shipped"

                    st.success(
                        f"{order.order_id} shipped."
                    )

                    st.rerun()