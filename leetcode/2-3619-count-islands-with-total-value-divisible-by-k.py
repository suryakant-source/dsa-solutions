# 3619. Count Islands With Total Value Divisible by K (Medium)
# Accepted: 2026-10-26 | AI-assisted practice
# Approach: Iterative DFS, sum each connected component
# Complexity: O(m*n) time, O(m*n) space
# Submission: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/submissions/2181825382/

from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue
                total = grid[r][c]
                grid[r][c] = 0
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for a, b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0 <= a < m and 0 <= b < n and grid[a][b]:
                            total += grid[a][b]
                            grid[a][b] = 0
                            stack.append((a, b))
                answer += total % k == 0
        return answer
