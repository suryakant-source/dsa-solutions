# LeetCode 300. Longest Increasing Subsequence
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 14:36 IST
# Pattern: Patience sorting: tails array with bisect_left.
# Complexity: O(n log n) time, O(n) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def lengthOfLIS(self, nums):
        tails=[]
        for x in nums:
            i=bisect_left(tails,x)
            if i==len(tails): tails.append(x)
            else: tails[i]=x
        return len(tails)
