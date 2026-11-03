# LeetCode 3736. Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Accepted as Suryakant_16 on 2026-11-03 06:13:37 IST (1016/1016 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        return sum(mx - x for x in nums)
