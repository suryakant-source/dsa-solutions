# LeetCode 2089. Find Target Indices After Sorting Array
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: sort, then scan for matches. Sort the array; the answer is the indices where value == target.
# Complexity: O(n log n) time, O(1) extra.
# Interview recall:
# - Sorting groups equal values together, so the matching indices are contiguous.
# - Alternative O(n) without sort: count elements < target (start) and == target.
# - Edge: target absent -> empty list.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, v in enumerate(nums) if v == target]
