import streamlit as st

from components.header import page_header


page_header(
    "Fulfillment Process",
    "The workflow this application is designed to support."
)


steps = [

    (
        "1",
        "Order received",
        "Orders enter the system and priority orders "
        "are clearly identified."
    ),

    (
        "2",
        "Order processed",
        "The office team reviews the order and "
        "confirms shipping requirements."
    ),

    (
        "3",
        "Inventory check",
        "Stock is checked in Main. If required stock "
        "is only in Overflow, a transfer is requested."
    ),

    (
        "4",
        "Picking",
        "The warehouse worker gets the product, "
        "variant, quantity and shelf location."
    ),

    (
        "5",
        "Packing verification",
        "Product, variant, quantity and shipping label "
        "are checked before packing is completed."
    ),

    (
        "6",
        "Staging",
        "Packed boxes receive a visible staging location "
        "and wait for courier pickup."
    ),

    (
        "7",
        "Shipping",
        "The package is marked shipped after courier handoff."
    ),

    (
        "8",
        "Exception management",
        "Stock, picking, packing and courier problems "
        "are logged and assigned rather than forgotten."
    )
]


for number, title, description in steps:

    with st.container(border=True):

        st.markdown(
            f"### {number}. {title}"
        )

        st.write(description)


st.markdown("## Design priorities")


st.write(
    """
    The application focuses on five operational priorities:

    **1. Visibility** — staff can see where orders are.

    **2. Priority control** — priority orders are separated
    from normal work.

    **3. Inventory accuracy** — Main and Overflow stock are
    visible and transferable.

    **4. Verification** — product, variant and quantity are
    confirmed before packing.

    **5. Exception management** — problems are recorded,
    assigned and resolved.
    """
)