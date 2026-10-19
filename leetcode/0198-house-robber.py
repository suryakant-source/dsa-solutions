# LeetCode 198. House Robber
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 11:39 IST
# Pattern: DP max of rob/skip per house.
# Complexity: O(n) time, O(1) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def rob(self, nums):
        a=b=0
        for x in nums: a,b=b,max(b,a+x)
        return b
