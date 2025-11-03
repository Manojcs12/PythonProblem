def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping:  # It's a closing bracket
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:  # It's an opening bracket
            stack.append(ch)

    return not stack  # valid if empty


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for s in test_cases:
        print(s, "->", is_valid(s))
