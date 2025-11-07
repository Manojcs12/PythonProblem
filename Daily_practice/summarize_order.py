def summarize_orders(orders: list[dict]) -> dict[str, float]:
    totals = {}

    for order in orders:
        # safely get user name
        user = order.get("user", {}).get("name")
        if not user:
            continue  # skip invalid entries

        # calculate total for this order
        order_total = 0.0
        for item in order.get("items", []):
            try:
                qty = item["quantity"]
                price = item["unit_price"]
                order_total += qty * price
            except KeyError:
                continue  # skip bad item records

        # add to cumulative total
        totals[user] = round(totals.get(user, 0) + order_total, 2)

    return totals


if __name__ == "__main__":
    orders = [
        {
            "order_id": "O1",
            "user": {"id": 1, "name": "Manoj"},
            "items": [
                {"product": "apple", "quantity": 3, "unit_price": 2.5},
                {"product": "banana", "quantity": 2, "unit_price": 3.0}
            ]
        },
        {
            "order_id": "O2",
            "user": {"id": 2, "name": "Priya"},
            "items": [
                {"product": "orange", "quantity": 5, "unit_price": 4.0}
            ]
        },
        {
            "order_id": "O3",
            "user": {"id": 1, "name": "Manoj"},
            "items": [
                {"product": "apple", "quantity": 1, "unit_price": 2.5}
            ]
        }
    ]
    print(summarize_orders(orders))
