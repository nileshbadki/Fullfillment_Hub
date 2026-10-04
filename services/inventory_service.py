def calculate_inventory(inventory):

    result = inventory.copy()

    result["available"] = (
        result["on_hand"]
        - result["reserved"]
    )

    result["stock_status"] = result.apply(
        lambda row:
            "Low Stock"
            if row["available"] <= row["reorder_level"]
            else "OK",
        axis=1
    )

    return result


def create_transfer(
    transfers,
    sku,
    product_name,
    from_warehouse,
    to_warehouse,
    quantity,
    requested_at
):

    transfer_id = (
        f"TR-{len(transfers) + 1:03d}"
    )

    new_row = {

        "transfer_id": transfer_id,

        "sku": sku,

        "product_name": product_name,

        "from_warehouse":
            from_warehouse,

        "to_warehouse":
            to_warehouse,

        "quantity":
            quantity,

        "status":
            "Requested",

        "requested_at":
            requested_at
    }

    return transfers._append(
        new_row,
        ignore_index=True
    )