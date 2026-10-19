# LeetCode 392. Is Subsequence
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 07:48 IST
# Pattern: Two pointers over s and t.
# Complexity: O(n) time, O(1) space.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch: i += 1
        return i == len(s)
