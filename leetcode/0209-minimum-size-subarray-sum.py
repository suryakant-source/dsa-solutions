# LeetCode 209. Minimum Size Subarray Sum
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 21:45 IST

from collections import Counter, defaultdict

class Solution:
    def minSubArrayLen(self, target, nums):
        left = total = 0
        best = len(nums)+1
        for right,x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best,right-left+1)
                total -= nums[left]
                left += 1
        return 0 if best > len(nums) else best
