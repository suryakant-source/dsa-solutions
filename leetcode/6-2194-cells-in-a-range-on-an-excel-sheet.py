# 2194. Cells in a Range on an Excel Sheet
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/submissions/2182210174/
from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(c)+str(r) for c in range(ord(s[0]), ord(s[3])+1) for r in range(int(s[1]), int(s[4])+1)]

