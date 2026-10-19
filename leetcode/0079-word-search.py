# LeetCode 79. Word Search
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 19:49 IST
# Pattern: Grid DFS with temporary visited marks, restore after.
# Complexity: O(R*C*4^L) time, O(L) aux.

class Solution:
    def exist(self, board, word):
        rows,cols = len(board),len(board[0])
        if len(word)>rows*cols: return False
        def dfs(r,c,i):
            if not (0<=r<rows and 0<=c<cols) or board[r][c]!=word[i]: return False
            if i==len(word)-1: return True
            old=board[r][c]
            board[r][c]='#'
            found = any(dfs(r+dr,c+dc,i+1) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)])
            board[r][c]=old
            return found
        return any(dfs(r,c,0) for r in range(rows) for c in range(cols))
