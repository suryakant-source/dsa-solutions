# LeetCode 2560. House Robber IV
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (capability) + greedy non-adjacent take. Time O(n log range), space O(1).
# - For a capability x, the robber can take any house with value <= x; greedy take-and-skip maximizes the count.
# - Feasible if that count reaches k; monotone in x, so binary search.
# - Greedy works because taking an eligible house never hurts: skipping it cannot free up more than one extra house.

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def ok(x):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
