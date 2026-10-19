# LeetCode 746. Min Cost Climbing Stairs
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 11:05 IST
# Pattern: DP: min cost to reach each step from either predecessor.
# Complexity: O(n) time, O(1) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def minCostClimbingStairs(self, cost):
        a=b=0
        for i in range(2,len(cost)+1): a,b=b,min(b+cost[i-1],a+cost[i-2])
        return b
