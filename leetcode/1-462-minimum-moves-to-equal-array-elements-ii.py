# LeetCode 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Accepted as Suryakant_16 on 2026-11-02 07:23:40 IST (33/33 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)
