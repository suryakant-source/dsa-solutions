# LeetCode 668. Kth Smallest Number in Multiplication Table
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: binary search on the answer + per-row counting. Time O(m log(mn)), space O(1).
# - Numbers <= x in row i: min(x // i, n); sum over rows is monotone in x.
# - Binary search the smallest x with count >= k; that x is a table entry.
# - No need to build the table at all.

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            return sum(min(x // i, n) for i in range(1, m + 1))
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
