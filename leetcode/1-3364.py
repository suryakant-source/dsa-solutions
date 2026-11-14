# LeetCode 3364. Minimum Positive Sum Subarray 
# https://leetcode.com/problems/minimum-positive-sum-subarray/
# Accepted as Suryakant_16 on 2026-11-14 07:24:40 IST (889/889 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = None
        for i in range(n):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]
                if j - i + 1 >= l and s > 0:
                    if best is None or s < best:
                        best = s
        return best if best is not None else -1
