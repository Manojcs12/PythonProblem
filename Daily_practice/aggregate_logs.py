def aggregate_logs(logs: list[dict]) -> dict[str, dict[str, int]]:
    outer_dict = {}
    for log in logs:
        system = log['system']
        category = log['category']
        count = log['count']

        # Initialize nested dict if not present
        if system not in outer_dict:
            outer_dict[system] = {}

        # Aggregate counts
        outer_dict[system][category] = outer_dict[system].get(category, 0) + count

    return outer_dict


if __name__ == "__main__":
    logs = [
        {"system": "serverA", "category": "error", "count": 5},
        {"system": "serverA", "category": "warning", "count": 2},
        {"system": "serverA", "category": "error", "count": 7},
        {"system": "serverB", "category": "info", "count": 5},
        {"system": "serverB", "category": "error", "count": 7}
    ]

    print(aggregate_logs(logs))
