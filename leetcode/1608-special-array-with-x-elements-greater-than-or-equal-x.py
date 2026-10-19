# LeetCode 1608. Special Array With X Elements Greater Than or Equal X
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: sort + binary search for the first index with nums[i] >= x, per candidate x.
# Time O(n log n), space O(1) extra.
# Interview recall:
# - x is bounded by n, so only n+1 candidates to test.
# - After sorting, count of elements >= x is n - lower_bound(x).
# - Answer is unique if it exists, so the first match can be returned.

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= x:
                    hi = mid
                else:
                    lo = mid + 1
            if n - lo == x:
                return x
        return -1
