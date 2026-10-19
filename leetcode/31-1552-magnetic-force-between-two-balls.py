# LeetCode 1552. Magnetic Force Between Two Balls
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: sort + binary search on the answer (minimum distance) + greedy placement. Time O(n log n + n log range), space O(1).
# - Place the first ball at the leftmost basket, then each next ball at the earliest position at least d away.
# - Feasible if m balls fit; monotone in d, so binary search the max feasible d.
# - Classic aggressive cows template.

class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        def ok(d):
            cnt = 1
            last = position[0]
            for p in position[1:]:
                if p - last >= d:
                    cnt += 1
                    last = p
            return cnt >= m
        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
