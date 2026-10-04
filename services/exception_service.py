def create_exception(
    exceptions,
    order_id,
    exception_type,
    severity,
    problem,
    owner,
    action,
    created_at
):

    exception_id = (
        f"EX-{len(exceptions) + 1:03d}"
    )

    row = {

        "exception_id":
            exception_id,

        "order_id":
            order_id,

        "type":
            exception_type,

        "severity":
            severity,

        "problem":
            problem,

        "owner":
            owner,

        "action":
            action,

        "status":
            "Open",

        "created_at":
            created_at
    }

    return exceptions._append(
        row,
        ignore_index=True
    )


def resolve_exception(
    exceptions,
    exception_id
):

    exceptions.loc[
        exceptions["exception_id"] == exception_id,
        "status"
    ] = "Resolved"

    return exceptions