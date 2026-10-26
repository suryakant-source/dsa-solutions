# 2798. Number of Employees Who Met the Target
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/2182307034/
from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)

