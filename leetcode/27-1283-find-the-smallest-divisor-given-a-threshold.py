# LeetCode 1283. Find the Smallest Divisor Given a Threshold
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (divisor). Time O(n log max), space O(1).
# - Sum of ceil(v/d) is monotone non-increasing in d, so the first feasible d is a lower-bound search.
# - Ceiling without floats: (v + d - 1) // d.
# - Search range is [1, max(nums)].

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def ok(d):
            return sum((v + d - 1) // d for v in nums) <= threshold
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
