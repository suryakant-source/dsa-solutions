# LeetCode 278. First Bad Version
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: classic binary search, lower bound on a monotone predicate.
# Time O(log n), space O(1).
# Interview recall:
# - Predicate is monotone (once bad, always bad) -> binary search for the first true.
# - hi = mid when bad (keep mid as candidate), lo = mid + 1 when good; loop ends at lo == hi.
# - Minimizes API calls; answer is lo.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
