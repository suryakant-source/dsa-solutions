# LeetCode 1200. Minimum Absolute Difference
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: sort; min difference must be between adjacent elements; collect all adjacent pairs achieving it.
# Complexity: O(n log n) time, O(n) output.
# Interview recall:
# - In a sorted array the closest pair of values is always adjacent.
# - Two passes: find min gap, then emit pairs with that gap (pairs come out sorted automatically).
# - Edge: duplicates give gap 0.

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        best = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == best]
