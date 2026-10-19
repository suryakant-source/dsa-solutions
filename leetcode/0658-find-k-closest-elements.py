# LeetCode 658. Find K Closest Elements
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search over window starts (window of size k).
# Time O(log(n-k) + k), space O(1) extra.
# Interview recall:
# - The answer is one contiguous window; search its left edge in [0, n-k].
# - Compare distances at the two window ends: x - arr[mid] vs arr[mid+k] - x.
# - Ties break toward the smaller value, which is why the comparison keeps lo's side on equality.

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]
