# LeetCode 268. Missing Number
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 23:57 IST
# Pattern: Sum formula n(n+1)/2 minus actual sum (or XOR).
# Complexity: O(n) time, O(1) space.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
