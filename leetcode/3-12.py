# LeetCode 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
# Accepted as Suryakant_16 on 2026-11-19 13:30:35 IST (3999/3999 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        out = []
        for v, s in vals:
            while num >= v:
                out.append(s)
                num -= v
        return "".join(out)
