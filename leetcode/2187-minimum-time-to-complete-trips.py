# LeetCode 2187. Minimum Time to Complete Trips
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (time). Time O(n log(min(time)*totalTrips)), space O(1).
# - Trips completed by time T is sum(T // t_i), monotone in T.
# - Binary search the smallest T reaching totalTrips.
# - Upper bound min(time)*totalTrips keeps the range tight.

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        lo, hi = 1, min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(mid // t for t in time) >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
