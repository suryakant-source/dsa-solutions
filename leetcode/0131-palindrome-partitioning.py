# LeetCode 131. Palindrome Partitioning
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 19:28 IST
# Pattern: Backtracking; recurse only on palindrome prefixes.
# Complexity: O(n*2^n) upper bound.

class Solution:
    def partition(self, s):
        out = []
        def dfs(start,path):
            if start==len(s):
                out.append(path[:])
                return
            for end in range(start+1,len(s)+1):
                t=s[start:end]
                if t==t[::-1]:
                    path.append(t)
                    dfs(end,path)
                    path.pop()
        dfs(0,[])
        return out
