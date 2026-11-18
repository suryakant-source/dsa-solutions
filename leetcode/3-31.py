# LeetCode 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# Accepted as Suryakant_16 on 2026-11-18 13:28:11 IST (268/268 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
