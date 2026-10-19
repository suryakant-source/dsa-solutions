# LeetCode 46. Permutations
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 15:41 IST
# Pattern: Backtracking with swap-in-place.
# Complexity: O(n*n!) time, O(n) aux.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def go(cur, rest):
            if not rest:
                res.append(cur); return
            for i in range(len(rest)):
                go(cur + [rest[i]], rest[:i] + rest[i+1:])
        go([], nums)
        return res
