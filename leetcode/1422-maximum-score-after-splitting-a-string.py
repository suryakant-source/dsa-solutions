class Solution:
    def maxScore(self, s: str) -> int:
        best = 0
        for i in range(1, len(s)):
            best = max(best, s[:i].count("0") + s[i:].count("1"))
        return best
