# LeetCode 740. Delete and Earn
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 12:38 IST
# Pattern: Aggregate points per value, then house-robber DP over values.
# Complexity: O(n + k) time, k = value range.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def deleteAndEarn(self, nums):
        points=[0]*(max(nums)+1)
        for x in nums: points[x]+=x
        a=b=0
        for x in points: a,b=b,max(b,a+x)
        return b
