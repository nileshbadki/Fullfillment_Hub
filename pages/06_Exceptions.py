import streamlit as st

from components.header import page_header
from components.metric_card import metric_card

from services.exception_service import (
    create_exception,
    resolve_exception
)

from utils.helpers import now_text


page_header(
    "Exceptions",
    "Make operational problems visible, assigned "
    "and trackable instead of informal."
)


data = st.session_state.data

exceptions = data["exceptions"]


open_count = len(
    exceptions[
        exceptions.status == "Open"
    ]
)

high_count = len(
    exceptions[
        exceptions.severity == "High"
    ]
)

resolved_count = len(
    exceptions[
        exceptions.status == "Resolved"
    ]
)


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        "Open",
        open_count,
        "Need action"
    )


with col2:

    metric_card(
        "High Severity",
        high_count,
        "Operational risk"
    )


with col3:

    metric_card(
        "Resolved",
        resolved_count,
        "Closed"
    )


st.markdown("## Exception log")


st.dataframe(
    exceptions,
    use_container_width=True,
    hide_index=True
)


st.markdown("## Resolve exception")


open_exceptions = exceptions[
    exceptions.status == "Open"
]


if not open_exceptions.empty:

    selected = st.selectbox(
        "Exception",
        open_exceptions.exception_id.tolist()
    )


    if st.button(
        "Mark Resolved",
        type="primary"
    ):

        data["exceptions"] = (
            resolve_exception(
                exceptions,
                selected
            )
        )

        st.success(
            f"{selected} resolved."
        )

        st.rerun()


st.markdown("## Log new exception")


with st.form("new_exception"):

    order_id = st.selectbox(
        "Order",
        data["orders"].order_id.tolist()
    )

    exception_type = st.selectbox(
        "Problem type",
        [
            "Priority deadline risk",
            "Stock discrepancy",
            "Wrong product",
            "Wrong variant",
            "Package misplaced",
            "Courier pickup missed",
            "Picking delay",
            "Packing issue",
            "Other"
        ]
    )

    severity = st.selectbox(
        "Severity",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    problem = st.text_area(
        "What happened?"
    )

    owner = st.selectbox(
        "Owner",
        [
            "Operations",
            "Warehouse",
            "Office Processor"
        ]
    )

    action = st.text_input(
        "Next action"
    )


    submitted = st.form_submit_button(
        "Create Exception"
    )


    if submitted:

        if not problem.strip():

            st.error(
                "Please describe the problem."
            )

        else:

            data["exceptions"] = (
                create_exception(
                    exceptions,
                    order_id,
                    exception_type,
                    severity,
                    problem,
                    owner,
                    action,
                    now_text()
                )
            )

            st.success(
                "Exception created."
            )

            st.rerun()