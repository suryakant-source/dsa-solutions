# LeetCode 90. Subsets II
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 18:06 IST
# Pattern: Sort, then skip duplicate siblings at the same recursion level.
# Complexity: O(n*2^n) time, O(n) aux.

class Solution:
    def subsetsWithDup(self, nums):
        a = sorted(nums)
        out = []
        def dfs(start,path):
            out.append(path[:])
            for i in range(start,len(a)):
                if i>start and a[i]==a[i-1]: continue
                path.append(a[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return out
