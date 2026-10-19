# LeetCode 976. Largest Perimeter Triangle
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: sort, scan triples from the largest side down; first valid triple is optimal.
# Complexity: O(n log n) time, O(1) extra.
# Interview recall:
# - Triangle inequality only needs a + b > c when c is the largest side.
# - After sorting, check consecutive triples from the end; the first valid one maximizes perimeter.
# - Edge: no valid triple -> 0.

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0
