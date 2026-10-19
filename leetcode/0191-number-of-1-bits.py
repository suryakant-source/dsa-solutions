# LeetCode 191. Number Of 1 Bits
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:56 IST

from collections import Counter, defaultdict

class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
