# LeetCode 202. Happy Number
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:49 IST

from collections import Counter, defaultdict

class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))
        return n==1
