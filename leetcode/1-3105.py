# LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Accepted as Suryakant_16 on 2026-11-12 07:26:46 IST (868/868 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = 1
        inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best
