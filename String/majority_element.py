# Boyer–Moore Voting Algorithm
def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate



if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    output = majority_element(nums)
    print(output)
