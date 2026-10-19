# LeetCode 1051. Height Checker
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: compare array against its sorted copy, count mismatches.
# Complexity: O(n log n) time, O(n) space.
# Interview recall:
# - The expected lineup is exactly sorted(heights); count positions that differ.
# - Counting sort variant exists (heights <= 100) for O(n).
# - Edge: already sorted -> 0.

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        exp = sorted(heights)
        return sum(1 for a, b in zip(heights, exp) if a != b)
