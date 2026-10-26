# 2011. Final Value of Variable After Performing Operations
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/submissions/2182016555/
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)

