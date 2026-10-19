# LeetCode 350. Intersection Of Two Arrays Ii
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:08 IST

from collections import Counter, defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        return list((Counter(nums1)&Counter(nums2)).elements())
