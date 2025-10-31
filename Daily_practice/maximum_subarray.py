def max_subarray(nums: list[int]) -> int:
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # Either extend the current subarray or start fresh at this element
        current_sum = max(num, current_sum + num)
        # Track the best so far
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = [5, 4, -1, 7, 8]
    print(max_subarray(nums))  # Output: 23


# Correct Approach — Kadane’s Algorithm (O(n))
# We maintain:
# current_sum: the best sum ending at this position
# max_sum: the best sum seen so far
# Idea:
# At each number, you decide:
# Should I add this number to the existing subarray, or start a new one here?