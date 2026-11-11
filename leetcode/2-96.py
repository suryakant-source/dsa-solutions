# LeetCode 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
# Accepted as Suryakant_16 on 2026-11-10 10:30:59 IST (19/19 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
