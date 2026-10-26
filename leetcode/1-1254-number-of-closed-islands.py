# 1254. Number of Closed Islands
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/number-of-closed-islands/submissions/2181681633/
from typing import List

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def fill(i, j):
            if grid[i][j] != 0:
                return
            stack = [(i, j)]
            grid[i][j] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a = x + dx
                    b = y + dy
                    if 0 <= a < m and 0 <= b < n and grid[a][b] == 0:
                        grid[a][b] = 1
                        stack.append((a, b))
        for i in range(m):
            fill(i, 0)
            fill(i, n - 1)
        for j in range(n):
            fill(0, j)
            fill(m - 1, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
                    fill(i, j)
        return ans
