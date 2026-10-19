# LeetCode 744. Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: Binary search smallest letter greater than target with wraparound.
# Complexity: O(log n) time, O(1) space.

from bisect import bisect_left, bisect_right

class Solution:
    def nextGreatestLetter(self, letters, target):
        return letters[bisect_right(letters,target)%len(letters)]
