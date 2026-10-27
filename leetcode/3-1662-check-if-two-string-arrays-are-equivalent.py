# LeetCode 1662: check-if-two-string-arrays-are-equivalent
# Accepted 2026-10-27T14:12:20+05:30. AI-assisted practice solution.
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
