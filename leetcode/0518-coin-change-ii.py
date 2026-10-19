# LeetCode 518. Coin Change II
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 13:54 IST
# Pattern: DP count combinations; iterate coins outer to avoid permutations.
# Complexity: O(amount*coins) time, O(amount) space.

from bisect import bisect_left, bisect_right
from collections import deque
from math import isqrt

class Solution:
    def change(self, amount, coins):
        dp=[1]+[0]*amount
        for c in coins:
            for a in range(c,amount+1): dp[a]+=dp[a-c]
        return dp[amount]
