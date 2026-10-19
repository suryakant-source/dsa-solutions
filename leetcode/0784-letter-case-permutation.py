# LeetCode 784. Letter Case Permutation
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 20:51 IST
# Pattern: Branch lower/upper for each letter, copy digits.
# Complexity: O(2^L) output time.

class Solution:
    def letterCasePermutation(self, s):
        out=['']
        for c in s:
            choices=(c.lower(),c.upper()) if c.isalpha() else (c,)
            out=[p+x for p in out for x in choices]
        return out
