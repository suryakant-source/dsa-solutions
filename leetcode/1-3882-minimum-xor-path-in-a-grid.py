# LeetCode 3882. Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/
# Accepted on LeetCode as Suryakant_16 on 2026-10-28 07:26 IST (999/999 testcases passed)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [set() for _ in range(n)]
        for i in range(m):
            cur = [set() for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    cur[j].add(v)
                else:
                    if i:
                        cur[j] |= {x ^ v for x in prev[j]}
                    if j:
                        cur[j] |= {x ^ v for x in cur[j - 1]}
            prev = cur
        return min(prev[n - 1])
