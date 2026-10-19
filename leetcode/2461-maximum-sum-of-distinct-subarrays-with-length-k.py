# LeetCode 2461. Maximum Sum Of Distinct Subarrays With Length K
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 21:39 IST

from collections import Counter, defaultdict

class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = {}
        total = best = 0
        for i,x in enumerate(nums):
            total += x
            freq[x] = freq.get(x,0)+1
            if i >= k:
                old = nums[i-k]
                total -= old
                freq[old] -= 1
                if not freq[old]: del freq[old]
            if i >= k-1 and len(freq)==k: best = max(best,total)
        return best
