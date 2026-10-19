# LeetCode 290. Word Pattern
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 00:55 IST

from collections import Counter, defaultdict

class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words) != len(pattern): return False
        forward,backward = {},{}
        for a,b in zip(pattern,words):
            if forward.get(a,b) != b or backward.get(b,a) != a: return False
            forward[a],backward[b] = b,a
        return True
