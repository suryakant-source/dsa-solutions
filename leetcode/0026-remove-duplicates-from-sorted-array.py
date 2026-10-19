# LeetCode 26. Remove Duplicates From Sorted Array
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:33 IST

from collections import Counter, defaultdict

class Solution:
    def removeDuplicates(self, nums):
        write = 0
        for x in nums:
            if write == 0 or x != nums[write-1]:
                nums[write] = x
                write += 1
        return write
