# LeetCode 169. Majority Element
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:15 IST

from collections import Counter, defaultdict

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for x in nums:
            if count == 0: candidate = x
            count += 1 if x == candidate else -1
        return candidate
