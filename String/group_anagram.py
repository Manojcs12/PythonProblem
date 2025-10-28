from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    #Sort the letters alphabetically and use that as the key.

    grouped = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))  # unique representation for anagrams
        grouped[key].append(s)

    return list(grouped.values())

if __name__ == "__main__":
    s = ["eat","tea","tan","ate","nat","bat"]
    l= group_anagrams(s)
    print(l)


