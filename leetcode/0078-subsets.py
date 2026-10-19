# LeetCode 78. Subsets
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 17:35 IST
# Pattern: Iterative power set: each element doubles existing subsets.
# Complexity: O(n*2^n) time and output.

class Solution:
    def subsets(self, nums):
        out = [[]]
        for x in nums: out += [a+[x] for a in out]
        return out
