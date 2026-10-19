# LeetCode 878. Nth Magical Number
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: binary search + inclusion-exclusion with LCM. Time O(log(n*min(a,b))), space O(1).
# - Magical numbers <= x: x/a + x/b - x/lcm(a,b).
# - Binary search the smallest x with count >= n, then take it mod 1e9+7.
# - The answer is always a multiple of a or b, so the lower-bound search lands exactly on it.

import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l = a * b // math.gcd(a, b)
        lo, hi = 1, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid // a + mid // b - mid // l >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo % MOD
