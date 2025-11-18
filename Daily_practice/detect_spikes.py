def detect_spikes(events: list[dict], window: int, threshold: float) -> list[int]:
    if not events or window <= 0:
        return []

    # Prepare a list of counts in timestamp order
    counts = [e["count"] for e in events]
    timestamps = [e["timestamp"] for e in events]

    spikes = []

    for i in range(len(events)):
        # Need at least `window` previous points
        if i < window:
            continue

        prev_window = counts[i - window:i]
        avg_prev = sum(prev_window) / window
        limit = avg_prev * threshold

        if counts[i] > limit:
            spikes.append(timestamps[i])

    return spikes


if __name__ == "__main__":
    events = [
        {"timestamp": 1, "count": 5},
        {"timestamp": 2, "count": 6},
        {"timestamp": 3, "count": 7},
        {"timestamp": 4, "count": 50},  # spike
        {"timestamp": 5, "count": 8},
        {"timestamp": 6, "count": 70}  # spike
    ]

if __name__ == "__main__":
    events = [
        {"timestamp": 1, "count": 5},
        {"timestamp": 2, "count": 6},
        {"timestamp": 3, "count": 7},
        {"timestamp": 4, "count": 50},  # spike
        {"timestamp": 5, "count": 8},
        {"timestamp": 6, "count": 70}  # spike
    ]

    window = 3
    threshold = 2.5
    print(detect_spikes(events, window, threshold))
