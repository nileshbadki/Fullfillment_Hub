import streamlit as st

from components.header import page_header

from services.order_service import (
    get_next_statuses,
    update_order_status
)


page_header(
    "Orders",
    "Track orders and move them through "
    "the fulfillment workflow."
)


data = st.session_state.data

orders = data["orders"]


col1, col2, col3 = st.columns(3)


with col1:

    priority_filter = st.selectbox(
        "Priority",
        [
            "All",
            "Priority",
            "Standard"
        ]
    )


with col2:

    status_filter = st.selectbox(
        "Status",
        [
            "All"
        ] +
        sorted(
            orders.status.unique()
        )
    )


with col3:

    search = st.text_input(
        "Search order/customer"
    )


filtered = orders.copy()


if priority_filter != "All":

    filtered = filtered[
        filtered.priority ==
        priority_filter
    ]


if status_filter != "All":

    filtered = filtered[
        filtered.status ==
        status_filter
    ]


if search:

    filtered = filtered[
        filtered.apply(
            lambda row:
                search.lower()
                in (
                    str(row.order_id)
                    + " "
                    + str(row.customer_name)
                ).lower(),
            axis=1
        )
    ]


st.dataframe(
    filtered[
        [
            "order_id",
            "customer_name",
            "product_name",
            "variant",
            "quantity",
            "priority",
            "status",
            "warehouse",
            "pickup_deadline"
        ]
    ],
    use_container_width=True,
    hide_index=True
)


st.markdown("## Order details")


if filtered.empty:

    st.warning(
        "No orders match the selected filters."
    )

else:

    selected = st.selectbox(
        "Select order",
        filtered.order_id.tolist()
    )

    order = orders[
        orders.order_id == selected
    ].iloc[0]


    st.markdown(
        f"""
        ### {order.order_id}

        **Customer:** {order.customer_name}

        **Product:** {order.product_name}

        **Variant:** {order.variant}

        **Quantity:** {order.quantity}

        **Priority:** {order.priority}

        **Warehouse:** {order.warehouse}

        **Courier:** {order.shipping_method}

        **Pickup deadline:** {order.pickup_deadline}

        **Current status:** {order.status}
        """
    )


    st.markdown("### Order timeline")

    timeline = [
        ("Order received", True),
        (
            "Order processed",
            order.status not in ["New"]
        ),
        (
            "Picking",
            order.status in [
                "Picking",
                "Packing",
                "Packed",
                "Staged",
                "Shipped"
            ]
        ),
        (
            "Packing",
            order.status in [
                "Packing",
                "Packed",
                "Staged",
                "Shipped"
            ]
        ),
        (
            "Staging",
            order.status in [
                "Staged",
                "Shipped"
            ]
        ),
        (
            "Shipped",
            order.status == "Shipped"
        )
    ]


    for label, complete in timeline:

        symbol = "✓" if complete else "○"

        st.write(
            f"{symbol} {label}"
        )


    next_options = get_next_statuses(
        order.status
    )


    if next_options:

        new_status = st.selectbox(
            "Move order to",
            next_options
        )


        if st.button(
            "Update order",
            type="primary"
        ):

            st.session_state.data["orders"] = (
                update_order_status(
                    orders,
                    selected,
                    new_status
                )
            )

            st.success(
                f"{selected} moved to {new_status}."
            )

            st.rerun()