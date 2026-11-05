# LeetCode 1385. Find the Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Accepted as Suryakant_16 on 2026-11-05 07:27:41 IST (103/103 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        from bisect import bisect_left
        arr2.sort()
        count = 0
        for a in arr1:
            i = bisect_left(arr2, a)
            too_close = (i < len(arr2) and arr2[i] - a <= d) or (i > 0 and a - arr2[i - 1] <= d)
            if not too_close:
                count += 1
        return count
