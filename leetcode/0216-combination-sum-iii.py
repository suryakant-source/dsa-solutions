# LeetCode 216. Combination Sum III
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 20:30 IST
# Pattern: Choose k increasing values from 1..9 summing to n.
# Complexity: O(C(9,k)) bounded search.

class Solution:
    def combinationSum3(self, k, n):
        out=[]
        def dfs(start,left,path):
            if len(path)==k:
                if left==0: out.append(path[:])
                return
            for x in range(start,10):
                if x>left: break
                path.append(x)
                dfs(x+1,left-x,path)
                path.pop()
        dfs(1,n,[])
        return out
