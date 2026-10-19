# LeetCode 49. Group Anagrams
# Status: Accepted (Python3)
# Solved: Oct 19, 2026 23:35 IST

from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for c in s: counts[ord(c)-97] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())
