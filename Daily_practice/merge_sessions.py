
def merge_sessions(logs: list[dict], timeout: int) -> dict[str, list[tuple[int, int]]]:
    if not logs:
        return {}

    # Step 1: Group timestamps by user
    grouped = {}
    for log in logs:
        user = log["user"]
        ts = log["timestamp"]
        grouped.setdefault(user, []).append(ts)

    # Step 2: Sort timestamps for each user
    for user in grouped:
        grouped[user].sort()

    # Step 3: Merge sessions
    result = {}

    for user, timestamps in grouped.items():
        sessions = []
        start = timestamps[0]
        end = timestamps[0]

        for i in range(1, len(timestamps)):
            if timestamps[i] - timestamps[i - 1] <= timeout:
                # Continue the current session
                end = timestamps[i]
            else:
                # End session and start a new one
                sessions.append((start, end))
                start = timestamps[i]
                end = timestamps[i]

        # Append the last session
        sessions.append((start, end))

        result[user] = sessions

    return result


if __name__== "__main__":
    logs = [
        {"user": "alice", "timestamp": 1},
        {"user": "alice", "timestamp": 2},
        {"user": "alice", "timestamp": 10},
        {"user": "bob", "timestamp": 4},
        {"user": "bob", "timestamp": 6},
        {"user": "bob", "timestamp": 20}
    ]

    timeout = 3
    print(merge_sessions(logs,timeout))