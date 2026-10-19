# LeetCode 1588. Sum Of All Odd Length Subarrays
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 21:33 IST

from collections import Counter, defaultdict

class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        return sum(x*(((i+1)*(n-i)+1)//2) for i,x in enumerate(arr))
