# LeetCode 3693. Climbing Stairs II
https://leetcode.com/problems/climbing-stairs-ii/
# Accepted as Suryakant_16 on 2026-11-10 07:24:51 IST (1005/1005 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            c = costs[j - 1]
            for d in (1, 2, 3):
                i = j - d
                if i >= 0:
                    val = dp[i] + c + d * d
                    if val < dp[j]:
                        dp[j] = val
        return dp[n]
