# 1672. Richest Customer Wealth
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/richest-customer-wealth/submissions/2182088913/
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))

