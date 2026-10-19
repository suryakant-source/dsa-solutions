# LeetCode 1356. Sort Integers by The Number of 1 Bits
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: custom sort key (popcount asc, value asc).
# Complexity: O(n log n) time, O(1) extra.
# Interview recall:
# - bin(x).count('1') or x.bit_count() gives the popcount.
# - Tie-break is the integer value itself - a two-field tuple key.
# - Edge: 0 has zero bits and sorts first.

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
