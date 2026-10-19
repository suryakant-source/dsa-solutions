# LeetCode 47. Permutations II
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 20:09 IST
# Pattern: Sort + used array; skip duplicate when predecessor unused.
# Complexity: O(n*n!) time, O(n) aux.

class Solution:
    def permuteUnique(self, nums):
        a=sorted(nums)
        used=[False]*len(a)
        out=[]
        def dfs(path):
            if len(path)==len(a):
                out.append(path[:])
                return
            for i,x in enumerate(a):
                if used[i] or (i>0 and a[i]==a[i-1] and not used[i-1]): continue
                used[i]=True
                path.append(x)
                dfs(path)
                path.pop()
                used[i]=False
        dfs([])
        return out
