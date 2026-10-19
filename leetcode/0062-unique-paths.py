# LeetCode 62. Unique Paths
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 16:43 IST
# Pattern: Grid DP: paths[i][j] = top + left (or combinatorics C(m+n-2, m-1)).
# Complexity: O(mn) time.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for j in range(1, n):
                row[j] += row[j-1]
        return row[-1]
