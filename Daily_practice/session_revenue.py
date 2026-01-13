from collections import defaultdict


def attribute_revenue(sessions: list[dict], purchases: list[dict]) -> dict[str, float]:
    # Group sessions and purchases by user
    sessions_by_user = defaultdict(list)
    purchases_by_user = defaultdict(list)

    for s in sessions:
        sessions_by_user[s["user"]].append(s)

    for p in purchases:
        purchases_by_user[p["user"]].append(p)

    result = defaultdict(float)

    # Process per user
    for user in sessions_by_user:
        user_sessions = sessions_by_user[user]
        user_purchases = purchases_by_user.get(user, [])

        # Sort per user
        user_sessions.sort(key=lambda x: x["start"])
        user_purchases.sort(key=lambda x: x["timestamp"])

        i = 0  # pointer for purchases

        for session in user_sessions:
            while i < len(user_purchases) and user_purchases[i]["timestamp"] < session["start"]:
                i += 1

            j = i
            while j < len(user_purchases) and user_purchases[j]["timestamp"] <= session["end"]:
                result[session["session_id"]] += user_purchases[j]["amount"]
                j += 1

            i = j  # advance pointer

    return dict(result)


if __name__ == "__main__":
    sessions = [
        {"user": "alice", "session_id": "S1", "start": 1, "end": 5},
        {"user": "alice", "session_id": "S2", "start": 10, "end": 15},
        {"user": "bob", "session_id": "S3", "start": 3, "end": 8}
    ]

    purchases = [
        {"user": "alice", "timestamp": 2, "amount": 50.0},
        {"user": "alice", "timestamp": 6, "amount": 30.0},
        {"user": "alice", "timestamp": 12, "amount": 70.0},
        {"user": "bob", "timestamp": 4, "amount": 20.0},
        {"user": "bob", "timestamp": 9, "amount": 100.0}
    ]
    print(attribute_revenue(sessions, purchases))
