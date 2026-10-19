# LeetCode 58. Length Of Last Word
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:10 IST

from collections import Counter, defaultdict

class Solution:
    def lengthOfLastWord(self, s):
        i = len(s)-1
        while s[i]==' ': i -= 1
        end = i
        while i >= 0 and s[i]!=' ': i -= 1
        return end-i
