# LeetCode 410. Split Array Largest Sum
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: binary search on the answer (minimized largest subarray sum) + greedy check.
# Time O(n log(sum)), space O(1).
# Interview recall:
# - Answer lies in [max(nums), sum(nums)]; feasibility (can we split into <= k groups under cap) is monotone.
# - Greedy check: fill each group until the cap, count groups.
# - Same template as Koko Eating Bananas / Capacity To Ship Packages / Min Days Bouquets.

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            groups, cur = 1, 0
            for v in nums:
                if cur + v > mid:
                    groups += 1
                    cur = 0
                cur += v
            if groups <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
