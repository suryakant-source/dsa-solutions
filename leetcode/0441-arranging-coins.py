# LeetCode 441. Arranging Coins
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: binary search on the answer (largest k with k(k+1)/2 <= n).
# Time O(log n), space O(1).
# Interview recall:
# - Total coins needed for k rows is the triangular number k(k+1)/2.
# - Monotone in k, so binary search; keep hi as the last feasible k.
# - Closed form also exists ((sqrt(8n+1)-1)/2), but binary search avoids float pitfalls.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            need = mid * (mid + 1) // 2
            if need <= n:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
