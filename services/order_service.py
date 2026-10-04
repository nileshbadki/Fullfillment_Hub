from utils.constants import STATUS_FLOW


def get_next_statuses(status):

    return STATUS_FLOW.get(
        status,
        []
    )


def update_order_status(
    orders,
    order_id,
    new_status
):

    orders.loc[
        orders["order_id"] == order_id,
        "status"
    ] = new_status

    return orders


def priority_orders(orders):

    return orders[
        (orders["priority"] == "Priority") &
        (orders["status"] != "Shipped")
    ].copy()


def orders_needing_attention(orders):

    return orders[
        (
            orders["priority"] == "Priority"
        )
        |
        (
            orders["status"].isin(
                [
                    "Stock Issue",
                    "Pickup Missed"
                ]
            )
        )
    ].copy()