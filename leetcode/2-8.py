# LeetCode 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# Accepted as Suryakant_16 on 2026-11-19 10:36:07 IST (1096/1096 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == " ":
            i += 1
        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        lo, hi = -2 ** 31, 2 ** 31 - 1
        if num < lo:
            return lo
        if num > hi:
            return hi
        return num
