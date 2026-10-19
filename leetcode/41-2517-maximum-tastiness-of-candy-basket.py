# LeetCode 2517. Maximum Tastiness of Candy Basket
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: sort + binary search on the answer (min pairwise difference) + greedy check. Time O(n log n + n log range), space O(1).
# - After sorting, the best basket for a target gap d is built greedily left to right.
# - Feasibility (can we pick k items with all gaps >= d) is monotone in d.
# - Same shape as aggressive cows / magnetic force.

class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        price.sort()
        def ok(d):
            cnt = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= d:
                    cnt += 1
                    last = p
            return cnt >= k
        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
