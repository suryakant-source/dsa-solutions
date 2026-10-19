# LeetCode 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Binary search bounds: bisect_left for first, bisect_right-1 for last.
# Complexity: O(log n) time, O(1) space.

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums, target):
        l=bisect_left(nums,target)
        return [l,bisect_right(nums,target)-1] if l<len(nums) and nums[l]==target else [-1,-1]
