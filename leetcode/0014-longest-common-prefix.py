# LeetCode 14. Longest Common Prefix
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:02 IST

from collections import Counter, defaultdict

class Solution:
    def longestCommonPrefix(self, strs):
        for i,c in enumerate(strs[0]):
            if any(i >= len(s) or s[i]!=c for s in strs): return strs[0][:i]
        return strs[0]
