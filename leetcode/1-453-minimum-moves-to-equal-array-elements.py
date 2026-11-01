# LeetCode 453. Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Accepted as Suryakant_16 on 2026-11-01 07:24:39 IST (84/84 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        smallest = min(nums)
        return sum(x - smallest for x in nums)
