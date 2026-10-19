# LeetCode 416. Partition Equal Subset Sum
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 19:24 IST
# Pattern: Subset-sum DP to sum/2.
# Complexity: O(n*sum) time, O(sum) space.

class Solution:
    def canPartition(self, nums):
        total=sum(nums)
        if total%2: return False
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for x in nums:
            for t in range(target,x-1,-1): dp[t]=dp[t] or dp[t-x]
        return dp[target]
