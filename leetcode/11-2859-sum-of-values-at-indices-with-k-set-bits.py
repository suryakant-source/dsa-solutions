# 2859. Sum of Values at Indices With K Set Bits
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/submissions/2182131134/
from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(x for i, x in enumerate(nums) if i.bit_count() == k)

