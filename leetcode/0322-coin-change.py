# LeetCode 322. Coin Change
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 13:21 IST
# Pattern: DP min coins per amount, unbounded.
# Complexity: O(amount*coins) time, O(amount) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def coinChange(self, coins, amount):
        dp=[0]+[amount+1]*amount
        for a in range(1,amount+1):
            for c in coins:
                if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount]<=amount else -1
