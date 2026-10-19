# LeetCode 279. Perfect Squares
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 19:46 IST
# Pattern: DP: min squares per number, try each square (POTD Oct 16).
# Complexity: O(n*sqrt(n)) time, O(n) space.

from math import isqrt

class Solution:
    def numSquares(self, n):
        squares=[x*x for x in range(1,isqrt(n)+1)]
        dp=[0]+[n+1]*n
        for i in range(1,n+1):
            for x in squares:
                if x>i: break
                dp[i]=min(dp[i],dp[i-x]+1)
        return dp[n]
