# LeetCode 242. Valid Anagram
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 23:36 IST
# Pattern: Frequency counter compare.
# Complexity: O(n) time, O(1) space.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
