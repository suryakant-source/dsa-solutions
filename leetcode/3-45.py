# LeetCode 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted as Suryakant_16 on 2026-11-21 13:35:50 IST (111/111 testcases)
# Practice solution written with AI assistance for daily DSA practice

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        far = 0
        for i in range(len(nums) - 1):
            if i + nums[i] > far:
                far = i + nums[i]
            if i == cur_end:
                jumps += 1
                cur_end = far
        return jumps
