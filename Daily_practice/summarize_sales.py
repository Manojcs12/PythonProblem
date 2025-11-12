def summarize_sales(sales: list[dict]) -> dict[str, dict[str, float]]:
    outer_dict = {}
    for sale in sales:
        region = sale['region']
        product = sale['product']
        total = sale['quantity'] * sale['unit_price']

        if region not in outer_dict:
            outer_dict[region] = {}
        outer_dict[region][product] = outer_dict[region].get(product, 0) + total

    # Sort each region’s inner dictionary by product name
    for region in outer_dict:
        outer_dict[region] = dict(sorted(outer_dict[region].items()))

    return outer_dict


if __name__ == "__main__":
    sales = [
        {"region": "EU", "product": "apple", "quantity": 10, "unit_price": 2.5},
        {"region": "US", "product": "banana", "quantity": 5, "unit_price": 3.0},
        {"region": "EU", "product": "apple", "quantity": 4, "unit_price": 2.5},
        {"region": "EU", "product": "orange", "quantity": 8, "unit_price": 4.0},
        {"region": "US", "product": "apple", "quantity": 2, "unit_price": 2.5}
    ]
    print(summarize_sales(sales))
