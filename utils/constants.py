ORDER_STATUSES = [
    "New",
    "Picking",
    "Packing",
    "Packed",
    "Staged",
    "Shipped",
    "Stock Issue"
]


STATUS_FLOW = {

    "New": [
        "Picking",
        "Stock Issue"
    ],

    "Picking": [
        "Packing",
        "Stock Issue"
    ],

    "Packing": [
        "Packed",
        "Stock Issue"
    ],

    "Packed": [
        "Staged"
    ],

    "Staged": [
        "Shipped",
        "Pickup Missed"
    ],

    "Stock Issue": [
        "Picking",
        "New"
    ],

    "Pickup Missed": [
        "Staged"
    ],

    "Shipped": []
}