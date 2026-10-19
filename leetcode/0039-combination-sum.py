# LeetCode 39. Combination Sum
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 18:26 IST
# Pattern: Backtracking; recurse same index for unlimited reuse.
# Complexity: Exponential output, O(target/min) depth.

class Solution:
    def combinationSum(self, candidates, target):
        a = sorted(candidates)
        out = []
        def dfs(start,left,path):
            if left==0:
                out.append(path[:])
                return
            for i in range(start,len(a)):
                if a[i]>left: break
                path.append(a[i])
                dfs(i,left-a[i],path)
                path.pop()
        dfs(0,target,[])
        return out
