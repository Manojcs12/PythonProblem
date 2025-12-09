from collections import defaultdict


def rolling_unique_users(events: list[dict], window: int) -> dict[int, int]:
    if not events:
        return {}

    # Step 1: Sort events by timestamp
    events.sort(key=lambda x: x["timestamp"])

    # Sliding window pointers
    left = 0

    # Tracks counts of users currently in the window
    user_count = defaultdict(int)

    result = {}

    # Helper: get window start time for a given T
    def window_start(T):
        return T - window + 1

    # Step 2: Iterate through sorted events
    i = 0
    n = len(events)

    while i < n:
        current_ts = events[i]["timestamp"]

        # Process all events that occur at this timestamp
        while i < n and events[i]["timestamp"] == current_ts:
            user = events[i]["user"]
            user_count[user] += 1
            i += 1

        # Step 3: Slide left pointer to remove old events
        start_limit = window_start(current_ts)

        while left < n and events[left]["timestamp"] < start_limit:
            old_user = events[left]["user"]
            user_count[old_user] -= 1
            if user_count[old_user] == 0:
                del user_count[old_user]
            left += 1

        # Step 4: Record number of unique users at this timestamp
        result[current_ts] = len(user_count)

    return result


if __name__ == "__main__":
    events = [
        {"timestamp": 3, "user": "alice"},
        {"timestamp": 1, "user": "alice"},
        {"timestamp": 2, "user": "bob"},
        {"timestamp": 4, "user": "alice"},
        {"timestamp": 4, "user": "charlie"},
        {"timestamp": 6, "user": "bob"}
    ]

    window = 3
    print(rolling_unique_users(events, window))
