# LeetCode 2361. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Accepted as Suryakant_16 on 2026-11-16 07:25:44 IST (121/121 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nxt = ""
            for i in range(0, len(s), k):
                nxt += str(sum(int(d) for d in s[i:i + k]))
            s = nxt
        return s
