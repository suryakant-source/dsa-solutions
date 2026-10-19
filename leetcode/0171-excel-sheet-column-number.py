# LeetCode 171. Excel Sheet Column Number
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 02:10 IST

from collections import Counter, defaultdict

class Solution:
    def titleToNumber(self, columnTitle):
        ans = 0
        for c in columnTitle: ans = ans*26+ord(c)-64
        return ans
