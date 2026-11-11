# LeetCode 3789. Minimum Cost to Acquire Required Items
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Accepted as Suryakant_16 on 2026-11-11 07:24:43 IST (1002/1002 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(need1, need2)
        total = both * min(costBoth, cost1 + cost2)
        rem1 = need1 - both
        rem2 = need2 - both
        total += rem1 * min(cost1, costBoth)
        total += rem2 * min(cost2, costBoth)
        return total
