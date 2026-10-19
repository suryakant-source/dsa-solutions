# LeetCode 77. Combinations
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 17:45 IST
# Pattern: Backtracking choose k in increasing order.
# Complexity: O(k*C(n,k)) time, O(k) aux.

class Solution:
    def combine(self, n, k):
        out = []
        def dfs(start, path):
            if len(path)==k:
                out.append(path[:])
                return
            for x in range(start,n-(k-len(path))+2):
                path.append(x)
                dfs(x+1,path)
                path.pop()
        dfs(1,[])
        return out
