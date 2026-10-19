# LeetCode 724. Find Pivot Index
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 21:58 IST

from collections import Counter, defaultdict

class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i,x in enumerate(nums):
            if left == total-left-x: return i
            left += x
        return -1
