# LeetCode 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted as Suryakant_16 on 2026-11-16 13:30:05 IST (316/316 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                t = nums[i] + nums[lo] + nums[hi]
                if t == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif t < 0:
                    lo += 1
                else:
                    hi -= 1
        return res
