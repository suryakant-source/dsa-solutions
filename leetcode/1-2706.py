# LeetCode 2706. Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Accepted as Suryakant_16 on 2026-11-19 07:24:22 IST (70/70 testcases)
# Practice solution written with AI assistance for daily DSA practice

from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
