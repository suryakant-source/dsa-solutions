# LeetCode 88. Merge Sorted Array
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:47 IST

from collections import Counter, defaultdict

class Solution:
    def merge(self, nums1, m, nums2, n):
        i,j,w = m-1,n-1,m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1
