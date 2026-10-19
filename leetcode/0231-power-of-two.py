# LeetCode 231. Power Of Two
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:42 IST

from collections import Counter, defaultdict

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1))==0
