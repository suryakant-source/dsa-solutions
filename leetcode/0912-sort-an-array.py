# LeetCode 912. Sort an Array
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: implement a real sort - top-down merge sort.
# Complexity: O(n log n) time, O(n) space, stable.
# Interview recall:
# - Constraints (5e4, values +/-5e4) also allow counting sort in O(n + k).
# - Merge sort is the safe expected answer; quicksort worst case can TLE on crafted tests.
# - Split at mid, sort halves, merge with two pointers.

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out
