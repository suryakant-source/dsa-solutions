# LeetCode 2226. Maximum Candies Allocated to K Children
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (pile size). Time O(n log max), space O(1).
# - For pile size x, sum(c // x) children can be served; monotone in x.
# - Search the largest feasible x; 0 is a valid answer so keep lo=0 and test mid>=1.
# - A pile can not be merged, only split, which is exactly what c // x counts.

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        lo, hi = 0, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if sum(c // mid for c in candies) >= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
