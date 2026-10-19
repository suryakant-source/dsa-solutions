# LeetCode 162. Find Peak Element
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Binary search on a peak: move toward the larger neighbor.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def findPeakElement(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[m+1]: l=m+1
            else: r=m
        return l
