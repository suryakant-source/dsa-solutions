# LeetCode 2418. Sort the People
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: zip keys with values, sort by key descending.
# Complexity: O(n log n) time, O(n) space.
# Interview recall:
# - Heights are distinct, so no tie-break logic needed.
# - Sort the pairs, not indices, to keep it one line.
# - Edge: negative key trick sorts descending with the default ascending sort.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [n for n, h in sorted(zip(names, heights), key=lambda p: -p[1])]
