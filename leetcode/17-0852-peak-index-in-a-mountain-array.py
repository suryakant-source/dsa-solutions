# LeetCode 852. Peak Index in a Mountain Array
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Binary search the peak index in a mountain array.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def peakIndexInMountainArray(self, arr):
        l,r=0,len(arr)-1
        while l<r:
            m=(l+r)//2
            if arr[m]<arr[m+1]: l=m+1
            else: r=m
        return l
