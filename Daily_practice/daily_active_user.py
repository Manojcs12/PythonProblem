from collections import defaultdict


def daily_active_users(events: list[dict]) -> dict[str, int]:
    users_by_date = defaultdict(set)

    # Step 1: Group users by date
    for event in events:
        users_by_date[event["date"]].add(event["user"])

    # Step 2: Build sorted result with counts
    result = {}
    for date in sorted(users_by_date.keys()):
        result[date] = len(users_by_date[date])

    return result


if __name__ == "__main__":
    events = [
        {"date": "2024-01-01", "user": "alice"},
        {"date": "2024-01-01", "user": "bob"},
        {"date": "2024-01-01", "user": "alice"},
        {"date": "2024-01-03", "user": "alice"},
        {"date": "2024-01-03", "user": "charlie"},
        {"date": "2024-01-02", "user": "bob"}
    ]
    print(daily_active_users(events))
