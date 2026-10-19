# LeetCode 2616. Minimize the Maximum Difference of Pairs
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: sort + binary search on the answer (max allowed difference) + greedy adjacent pairing. Time O(n log n + n log range), space O(1).
# - After sorting, optimal pairs for a budget d are adjacent: greedy takes (i, i+1) whenever their diff <= d.
# - Feasible if we can form at least p pairs; monotone in d.
# - Adjacent greedy is optimal since crossing pairs can be uncrossed without increasing any difference.

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def ok(d):
            cnt = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
