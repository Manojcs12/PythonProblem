from collections import defaultdict, Counter


def top_events_by_category(logs: list[dict], top_n: int) -> dict[str, list[tuple[str, int]]]:
    # Step 1: Create a nested mapping {category: Counter(events)}
    category_counts = defaultdict(Counter)

    for log in logs:
        category = log["category"]
        event = log["event"]
        category_counts[category][event] += 1

    # Step 2: Build the output with top N events per category
    result = {}
    for category, counter in category_counts.items():
        # Sort: by count (desc), then event name (asc)
        sorted_events = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        result[category] = sorted_events[:top_n]

    return result


if __name__ == "__main__":
    logs = [
        {"category": "trade", "event": "order_placed"},
        {"category": "trade", "event": "order_placed"},
        {"category": "trade", "event": "order_cancelled"},
        {"category": "system", "event": "login"},
        {"category": "system", "event": "login"},
        {"category": "system", "event": "error"},
        {"category": "user", "event": "profile_updated"},
        {"category": "user", "event": "login"},
        {"category": "user", "event": "login"}
    ]
    print(top_events_by_category(logs, 2))
