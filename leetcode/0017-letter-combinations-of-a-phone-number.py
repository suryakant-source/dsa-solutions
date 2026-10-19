# LeetCode 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 19:08 IST
# Pattern: Extend prefix strings digit by digit.
# Complexity: O(4^d) output time.

class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        letters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        out = ['']
        for d in digits: out = [s+c for s in out for c in letters[d]]
        return out
