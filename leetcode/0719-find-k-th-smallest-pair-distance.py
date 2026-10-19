# LeetCode 719. Find K-th Smallest Pair Distance
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: sort + binary search on the answer + sliding-window pair counting. Time O(n log n + n log range), space O(1).
# - Pairs with distance <= d are counted with one two-pointer pass after sorting.
# - Count is monotone in d, so binary search the smallest d with at least k pairs.
# - The count pass is O(n) because the right pointer only moves forward.

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def count(d):
            cnt = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= d:
                    j += 1
                cnt += j - i - 1
            return cnt
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
