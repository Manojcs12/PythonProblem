def first_unique_char(s: str) -> int:
    from collections import Counter
    counts = Counter(s)
    print(counts)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


def first_unique_char2(s: str) -> int:
    # Step 1: Count occurrences manually
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: Find first index with frequency == 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


if __name__ == "__main__":
    s = "loveleetcode"
    print(first_unique_char(s))  # Output: 2
