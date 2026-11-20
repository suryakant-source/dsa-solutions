# LeetCode 3298. Maximize Consecutive Elements in an Array After Modification
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Accepted as Suryakant_16 on 2026-11-20 07:27:54 IST (668/668 testcases)
# Practice solution written with AI assistance for daily DSA practice

from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = {}
        best = 0
        for x in nums:
            fx = f.get(x, 0)
            fx1 = f.get(x - 1, 0)
            nxp1 = fx + 1
            nx = fx if fx > fx1 + 1 else fx1 + 1
            if nxp1 > f.get(x + 1, 0):
                f[x + 1] = nxp1
            if nx > fx:
                f[x] = nx
            if nxp1 > best:
                best = nxp1
            if nx > best:
                best = nx
        return best
