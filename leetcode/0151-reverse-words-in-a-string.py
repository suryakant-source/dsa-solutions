# LeetCode 151. Reverse Words In A String
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:23 IST

from collections import Counter, defaultdict

class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
