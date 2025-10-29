def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        print(complement)
        print(seen)
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    l = two_sum(nums, target)
    print(l)
