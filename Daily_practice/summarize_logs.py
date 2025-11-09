def summarize_logs(file_path: str) -> dict[str, int]:
    event_counts = {}

    try:
        with open(file_path, "r") as file:
            for line in file:
                # Clean & validate
                parts = [p.strip() for p in line.strip().split('|')]
                if len(parts) < 3:
                    continue  # skip malformed lines

                event = parts[2].upper()

                # Increment count
                event_counts[event] = event_counts.get(event, 0) + 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}

    return event_counts


if __name__ == "__main__":
    result = summarize_logs("events.log")
    print(result)
