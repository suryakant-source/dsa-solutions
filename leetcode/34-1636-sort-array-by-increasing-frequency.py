# LeetCode 1636. Sort Array by Increasing Frequency
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: frequency map + custom sort key (frequency asc, value desc).
# Complexity: O(n log n) time, O(n) space.
# Interview recall:
# - Counter gives frequencies; sort key is the tuple (freq[x], -x).
# - Sorting the original array keeps duplicates in place - no need to rebuild from groups.
# - Edge: negative values handled by the -x tie-break.

from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
