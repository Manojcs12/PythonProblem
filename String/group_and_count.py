def group_and_count(items: list[str]) -> dict[str, int]:
    grouped_dict = {}
    for item in items:
        if item in grouped_dict:
            grouped_dict[item] = grouped_dict[item] + 1
        else:
            grouped_dict[item] = 1
    keys = list(grouped_dict.keys())
    keys.sort()
    sd = {i: grouped_dict[i] for i in keys}
    return sd


# chatgpt code
def group_and_count2(items: list[str]) -> dict[str, int]:
    grouped = {}
    for item in items:
        grouped[item] = grouped.get(item, 0) + 1
    return {k: grouped[k] for k in sorted(grouped)}


if __name__ == "__main__":
    print(group_and_count(["apple", "banana", "apple", "orange", "banana", "apple"]))
