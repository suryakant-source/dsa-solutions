# LeetCode 205. Isomorphic Strings
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:42 IST

from collections import Counter, defaultdict

class Solution:
    def isIsomorphic(self, s, t):
        forward, backward = {}, {}
        for a,b in zip(s,t):
            if forward.get(a,b) != b or backward.get(b,a) != a: return False
            forward[a],backward[b] = b,a
        return True
