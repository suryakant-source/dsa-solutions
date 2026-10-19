# LeetCode 387. First Unique Character in a String
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 07:27 IST
# Pattern: Frequency map then first index with count 1.
# Complexity: O(n) time, O(1) space.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1: return i
        return -1
