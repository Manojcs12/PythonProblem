import pandas as pd

def top_products(records: list[dict], top_n: int) -> list[tuple[str, float]]:
    if not records or top_n <= 0:
        return []

    df = pd.DataFrame(records)
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Aggregate by product
    agg_df = (
        df.groupby("product", as_index=False)["revenue"]
        .sum()
        .sort_values(["revenue", "product"], ascending=[False, True])
    )

    # Take top N
    top_df = agg_df.head(top_n)

    return list(zip(top_df["product"], top_df["revenue"].round(2)))


if __name__ == "__main__":
    records = [
        {"product": "apple", "region": "EU", "quantity": 10, "unit_price": 2.5},
        {"product": "banana", "region": "US", "quantity": 5, "unit_price": 3.0},
        {"product": "apple", "region": "US", "quantity": 4, "unit_price": 2.5},
        {"product": "orange", "region": "EU", "quantity": 8, "unit_price": 4.0},
    ]
    print(top_products(records, 2))
