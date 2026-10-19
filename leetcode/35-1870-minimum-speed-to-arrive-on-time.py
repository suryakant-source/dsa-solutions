# LeetCode 1870. Minimum Speed to Arrive on Time
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (speed). Time O(n log 1e7), space O(1).
# - Every leg except the last costs ceil(d/s); the last leg is exact division (no waiting).
# - If hour <= len(dist) - 1 it is impossible: the ceiling terms alone already exceed hour.
# - Binary search the smallest feasible speed; compare in floats only for the final leg.

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        def ok(s):
            t = 0.0
            for d in dist[:-1]:
                t += (d + s - 1) // s
            t += dist[-1] / s
            return t <= hour
        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
