# LeetCode 383. Ransom Note
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:28 IST

from collections import Counter, defaultdict

class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not (Counter(ransomNote)-Counter(magazine))
