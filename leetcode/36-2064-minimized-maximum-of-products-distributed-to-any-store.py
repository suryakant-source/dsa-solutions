# LeetCode 2064. Minimized Maximum of Products Distributed to Any Store
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: binary search on the answer (max products per store). Time O(m log max), space O(1).
# - For a cap x, each product type needs ceil(q/x) stores; feasible if the total fits in n.
# - Feasibility is monotone in x, so binary search the smallest feasible cap.
# - Same template as Koko Eating Bananas and 1283.

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def ok(x):
            return sum((q + x - 1) // x for q in quantities) <= n
        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
