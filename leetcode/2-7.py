# LeetCode 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Accepted as Suryakant_16 on 2026-11-18 10:27:54 IST (1046/1046 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if -2 ** 31 <= rev <= 2 ** 31 - 1 else 0
