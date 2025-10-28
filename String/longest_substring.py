def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        print(range(len(s)))
        print(right)
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len = max(max_len, right- left+1)
    print(seen)
    return max_len


if __name__ == "__main__":
    s = "abcbcb"
    l= length_of_longest_substring(s)
    print(l)





