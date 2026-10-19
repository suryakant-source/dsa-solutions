# LeetCode 349. Intersection Of Two Arrays
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:02 IST

from collections import Counter, defaultdict

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))
