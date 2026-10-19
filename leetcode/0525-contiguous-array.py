# LeetCode 525. Contiguous Array
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:12 IST

from collections import Counter, defaultdict

class Solution:
    def findMaxLength(self, nums):
        first = {0:-1}
        balance = best = 0
        for i,x in enumerate(nums):
            balance += 1 if x else -1
            if balance in first: best = max(best,i-first[balance])
            else: first[balance] = i
        return best
