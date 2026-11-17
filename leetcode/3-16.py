# LeetCode 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/
# Accepted as Suryakant_16 on 2026-11-17 13:28:43 IST (110/110 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                t = nums[i] + nums[lo] + nums[hi]
                if abs(t - target) < abs(best - target):
                    best = t
                if t < target:
                    lo += 1
                elif t > target:
                    hi -= 1
                else:
                    return t
        return best
