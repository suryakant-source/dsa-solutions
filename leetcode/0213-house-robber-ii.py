# LeetCode 213. House Robber II
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 12:10 IST
# Pattern: Two linear house-robber passes: exclude first or exclude last.
# Complexity: O(n) time, O(1) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def rob(self, nums):
        if len(nums)==1: return nums[0]
        def linear(lo,hi):
            a=b=0
            for i in range(lo,hi): a,b=b,max(b,a+nums[i])
            return b
        return max(linear(0,len(nums)-1),linear(1,len(nums)))
