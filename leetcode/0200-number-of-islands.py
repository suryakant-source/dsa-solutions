# LeetCode 200. Number of Islands
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 22:15 IST
# Pattern: Flood fill from each unvisited land cell.
# Complexity: O(mn) time, O(mn) worst stack.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]); res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    st = [(i, j)]; grid[i][j] = '0'
                    while st:
                        x, y = st.pop()
                        for a, b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                                grid[a][b] = '0'; st.append((a, b))
        return res
