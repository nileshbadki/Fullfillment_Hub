import streamlit as st

from components.header import page_header
from components.metric_card import metric_card
from services.order_service import (
    priority_orders,
    orders_needing_attention
)


page_header(
    "Today's Operations",
    "See what needs attention before orders miss "
    "their fulfillment deadlines."
)


data = st.session_state.data

orders = data["orders"]
exceptions = data["exceptions"]
shipments = data["shipments"]


open_orders = len(
    orders[
        orders.status != "Shipped"
    ]
)


priority = priority_orders(
    orders
)


stock_issues = len(
    orders[
        orders.status == "Stock Issue"
    ]
)


open_exceptions = len(
    exceptions[
        exceptions.status == "Open"
    ]
)


ready = len(
    orders[
        orders.status.isin(
            ["Packed", "Staged"]
        )
    ]
)


columns = st.columns(5)


metrics = [

    (
        "Open Orders",
        open_orders,
        "Not shipped"
    ),

    (
        "Priority",
        len(priority),
        "Needs same-day attention"
    ),

    (
        "Stock Issues",
        stock_issues,
        "Orders currently blocked"
    ),

    (
        "Exceptions",
        open_exceptions,
        "Need action"
    ),

    (
        "Ready",
        ready,
        "Packed / staged"
    )
]


for col, metric in zip(
    columns,
    metrics
):

    with col:
        metric_card(*metric)


st.markdown("## 🔴 Priority queue")

if priority.empty:

    st.success(
        "No open priority orders."
    )

else:

    st.dataframe(
        priority[
            [
                "order_id",
                "customer_name",
                "product_name",
                "variant",
                "status",
                "pickup_deadline"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


st.markdown("## ⚠ Needs attention")


attention = orders_needing_attention(
    orders
)


if attention.empty:

    st.success(
        "No critical issues currently detected."
    )

else:

    st.dataframe(
        attention[
            [
                "order_id",
                "priority",
                "status",
                "warehouse",
                "pickup_deadline",
                "note"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


st.markdown("## Fulfillment pipeline")


pipeline = orders.status.value_counts()


cols = st.columns(7)

for col, status in zip(
    cols,
    [
        "New",
        "Picking",
        "Packing",
        "Packed",
        "Staged",
        "Shipped",
        "Stock Issue"
    ]
):

    with col:

        st.metric(
            status,
            int(pipeline.get(status, 0))
        )