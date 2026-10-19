# LeetCode 448. Find All Numbers Disappeared In An Array
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:21 IST

from collections import Counter, defaultdict

class Solution:
    def findDisappearedNumbers(self, nums):
        for x in nums:
            i = abs(x)-1
            nums[i] = -abs(nums[i])
        return [i+1 for i,x in enumerate(nums) if x > 0]
