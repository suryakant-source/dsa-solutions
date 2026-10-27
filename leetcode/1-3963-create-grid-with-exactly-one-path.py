# LeetCode 3963: create-grid-with-exactly-one-path
# Accepted 2026-10-27T07:23:37+05:30. AI-assisted practice solution.
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ['.' * n] + ['#' * (n - 1) + '.'] * (m - 1)
