import streamlit as st

from components.header import page_header
from components.metric_card import metric_card

from services.inventory_service import (
    calculate_inventory,
    create_transfer
)

from utils.helpers import now_text


page_header(
    "Inventory",
    "See what is available in Main and Overflow "
    "and move stock when the main warehouse needs it."
)


data = st.session_state.data

inventory = calculate_inventory(
    data["inventory"]
)

orders = data["orders"]


main = inventory[
    inventory.warehouse == "Main"
]

overflow = inventory[
    inventory.warehouse == "Overflow"
]


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        "Main Available",
        int(main.available.sum()),
        "Units"
    )


with col2:

    metric_card(
        "Overflow Available",
        int(overflow.available.sum()),
        "Units"
    )


with col3:

    metric_card(
        "Low Stock",
        int(
            (
                inventory.stock_status ==
                "Low Stock"
            ).sum()
        ),
        "Inventory rows"
    )


st.markdown("## Inventory")


st.dataframe(
    inventory,
    use_container_width=True,
    hide_index=True
)


st.markdown("## 🔴 Orders blocked by stock")


blocked = orders[
    orders.status == "Stock Issue"
]


if blocked.empty:

    st.success(
        "No orders currently blocked."
    )

else:

    for _, order in blocked.iterrows():

        st.markdown(
            f"""
            <div class="alert-card">

            <b>{order.order_id}</b>

            <br>

            {order.product_name} —
            {order.variant}

            <br>

            Required:
            <b>{order.quantity}</b>

            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("## Request stock transfer")


sku = st.selectbox(
    "Product",
    inventory.sku.tolist()
)


selected = inventory[
    inventory.sku == sku
].iloc[0]


st.write(
    f"**{selected.product_name}**"
)


quantity = st.number_input(
    "Quantity",
    min_value=1,
    max_value=100,
    value=1
)


if st.button(
    "Create Transfer Request",
    type="primary"
):

    data["transfers"] = create_transfer(
        data["transfers"],
        selected.sku,
        selected.product_name,
        "Overflow",
        "Main",
        quantity,
        now_text()
    )

    st.success(
        f"Transfer request created: "
        f"{quantity} × {selected.product_name}"
    )


st.markdown("## Transfer requests")


st.dataframe(
    data["transfers"],
    use_container_width=True,
    hide_index=True
)