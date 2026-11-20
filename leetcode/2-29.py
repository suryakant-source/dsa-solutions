# LeetCode 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# Accepted as Suryakant_16 on 2026-11-20 10:37:12 IST (994/994 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        lo = -1 << 31
        hi = (1 << 31) - 1
        neg = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        q = 0
        while a >= b:
            t, m = b, 1
            while a >= t << 1:
                t <<= 1
                m <<= 1
            a -= t
            q += m
        if neg:
            q = -q
        if q < lo:
            return lo
        if q > hi:
            return hi
        return q
