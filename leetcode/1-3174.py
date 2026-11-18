# LeetCode 3174. Minimum Number of Changes to Make Binary String Beautiful
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# Accepted as Suryakant_16 on 2026-11-18 07:24:54 IST (577/577 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
