# LeetCode 190. Reverse Bits
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 02:01 IST

from collections import Counter, defaultdict

class Solution:
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
            ans = (ans<<1)|(n&1)
            n >>= 1
        return ans
