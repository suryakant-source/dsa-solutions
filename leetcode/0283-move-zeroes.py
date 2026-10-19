# LeetCode 283. Move Zeroes
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:19 IST

from collections import Counter, defaultdict

class Solution:
    def moveZeroes(self, nums):
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write],nums[i] = nums[i],nums[write]
                write += 1
