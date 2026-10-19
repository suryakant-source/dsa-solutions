# LeetCode 1480. Running Sum Of 1d Array
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 21:52 IST

from collections import Counter, defaultdict

class Solution:
    def runningSum(self, nums):
        out = []
        total = 0
        for x in nums:
            total += x
            out.append(total)
        return out
