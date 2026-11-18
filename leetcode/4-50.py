# LeetCode 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Accepted as Suryakant_16 on 2026-11-18 16:39:15 IST (309/309 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = abs(n)
        res = 1.0
        while p:
            if p & 1:
                res *= x
            x *= x
            p >>= 1
        return res if n >= 0 else 1 / res
