# LeetCode 40. Combination Sum II
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 18:47 IST
# Pattern: Sort, single use, skip equal siblings.
# Complexity: O(2^n) upper bound, O(n) aux.

class Solution:
    def combinationSum2(self, candidates, target):
        a = sorted(candidates)
        out = []
        def dfs(start,left,path):
            if left==0:
                out.append(path[:])
                return
            for i in range(start,len(a)):
                if i>start and a[i]==a[i-1]: continue
                if a[i]>left: break
                path.append(a[i])
                dfs(i+1,left-a[i],path)
                path.pop()
        dfs(0,target,[])
        return out
