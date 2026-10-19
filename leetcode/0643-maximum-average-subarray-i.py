# LeetCode 643. Maximum Average Subarray I
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:06 IST

from collections import Counter, defaultdict

class Solution:
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        best = total
        for i in range(k,len(nums)):
            total += nums[i]-nums[i-k]
            best = max(best,total)
        return best/k
