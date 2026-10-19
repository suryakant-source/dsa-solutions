# LeetCode 27. Remove Element
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:40 IST

from collections import Counter, defaultdict

class Solution:
    def removeElement(self, nums, val):
        write = 0
        for x in nums:
            if x != val:
                nums[write] = x
                write += 1
        return write
