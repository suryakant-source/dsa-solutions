# LeetCode 136. Single Number
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 21:32 IST
# Pattern: XOR all values; pairs cancel.
# Complexity: O(n) time, O(1) space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for v in nums: r ^= v
        return r
