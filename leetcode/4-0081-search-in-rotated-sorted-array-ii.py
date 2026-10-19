# LeetCode 81. Search in Rotated Sorted Array II
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on a rotated array with duplicates.
# Time O(log n) average, O(n) worst (all duplicates), space O(1).
# Interview recall:
# - Duplicates break the sorted-half test: when nums[lo] == nums[mid] == nums[hi], shrink both ends.
# - Otherwise one half is sorted; check if the target lies inside it to pick the side.
# - Worst case degrades to linear scan, and that is unavoidable with duplicates.

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
