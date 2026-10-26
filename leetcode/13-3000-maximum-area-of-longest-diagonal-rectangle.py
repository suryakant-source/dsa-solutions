# 3000. Maximum Area of Longest Diagonal Rectangle
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/submissions/2181902072/
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((a*a+b*b, a*b) for a,b in dimensions)[1]

