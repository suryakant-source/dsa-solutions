# LeetCode 905. Sort Array By Parity
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 22:54 IST

from collections import Counter, defaultdict

class Solution:
    def sortArrayByParity(self, nums):
        return [x for x in nums if x%2==0]+[x for x in nums if x%2]
