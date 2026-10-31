# LeetCode 3665. Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/
# Accepted as Suryakant_16 on 2026-10-31 07:26:45 IST (521/521 testcases)
# Practice solution written with AI assistance for daily DSA practice

import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def mirror_land(x, y, entered_right):
            if entered_right:
                nx, ny, d = x + 1, y, False
            else:
                nx, ny, d = x, y + 1, True
            if nx >= m or ny >= n:
                return None
            if grid[nx][ny] == 1:
                return mirror_land(nx, ny, d)
            return (nx, ny)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            total = 0
            for di, dj, entered_right in ((0, 1, True), (1, 0, False)):
                ni, nj = i + di, j + dj
                if ni >= m or nj >= n:
                    continue
                if grid[ni][nj] == 1:
                    land = mirror_land(ni, nj, entered_right)
                    if land is None:
                        continue
                    ni, nj = land
                total = (total + dp(ni, nj)) % MOD
            return total

        return dp(0, 0)
