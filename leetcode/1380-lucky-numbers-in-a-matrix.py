class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        mins = {min(row) for row in matrix}
        maxs = {max(col) for col in zip(*matrix)}
        return list(mins & maxs)
