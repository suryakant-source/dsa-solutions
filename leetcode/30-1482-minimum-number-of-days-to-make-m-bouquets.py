# LeetCode 1482. Minimum Number of Days to Make m Bouquets
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (minimum day) + greedy feasibility.
# Time O(n log(max bloomDay)), space O(1).
# Interview recall:
# - If m*k > n, return -1 immediately.
# - Feasibility is monotone in days: more days can only bloom more flowers.
# - Greedy: walk once, count runs of k consecutive bloomed flowers as bouquets.

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            bouquets, run = 0, 0
            for d in bloomDay:
                if d <= mid:
                    run += 1
                    if run == k:
                        bouquets += 1
                        run = 0
                else:
                    run = 0
            if bouquets >= m:
                hi = mid
            else:
                lo = mid + 1
        return lo
