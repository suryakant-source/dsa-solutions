class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd = sum(1 for p in position if p % 2)
        return min(odd, len(position) - odd)
