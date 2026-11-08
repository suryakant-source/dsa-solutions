# LeetCode 1267. Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/
# Accepted as Suryakant_16 on 2026-11-08 07:25:32 IST (55/55 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count
