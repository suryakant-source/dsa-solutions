# LeetCode 452. Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: interval scheduling greedy - sort by end coordinate, shoot at the earliest end.
# Complexity: O(n log n) time, O(1) extra.
# Interview recall:
# - Sorting by end (not start) is what makes the greedy optimal.
# - Each new balloon whose start is past the current arrow position forces a new arrow.
# - Edge: touching endpoints count as burst (s > end means strictly past).

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arrows = 0
        end = None
        for s, e in points:
            if end is None or s > end:
                arrows += 1
                end = e
        return arrows
