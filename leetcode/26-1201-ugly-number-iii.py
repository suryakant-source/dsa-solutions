# LeetCode 1201. Ugly Number III
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search + inclusion-exclusion counting. Time O(log(2e9)), space O(1).
# - Count of ugly numbers <= x is x/a + x/b + x/c - x/lcm(a,b) - x/lcm(b,c) - x/lcm(a,c) + x/lcm(a,b,c).
# - Count is monotone in x, so binary search the smallest x with count >= n; that x is itself ugly.
# - LCMs come from GCDs to avoid overflow-prone products.

import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // math.gcd(a, b)
        bc = b * c // math.gcd(b, c)
        ac = a * c // math.gcd(a, c)
        abc = ab * c // math.gcd(ab, c)
        def count(x):
            return x // a + x // b + x // c - x // ab - x // bc - x // ac + x // abc
        lo, hi = 1, 2 * 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
