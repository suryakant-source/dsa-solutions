# LeetCode 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted as Suryakant_16 on 2026-11-17 10:29:42 IST (1158/1158 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        r, step = 0, 1
        for ch in s:
            rows[r].append(ch)
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step
        return "".join("".join(row) for row in rows)
