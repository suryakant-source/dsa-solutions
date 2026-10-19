# LeetCode 412. Fizz Buzz
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:37 IST

from collections import Counter, defaultdict

class Solution:
    def fizzBuzz(self, n):
        return [('Fizz'*(i%3==0)+'Buzz'*(i%5==0)) or str(i) for i in range(1,n+1)]
