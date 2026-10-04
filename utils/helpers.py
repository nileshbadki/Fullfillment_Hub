from datetime import datetime


def now_text():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )


def calculate_available(on_hand, reserved):

    return max(
        int(on_hand) - int(reserved),
        0
    )