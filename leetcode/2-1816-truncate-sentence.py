# LeetCode 1816: truncate-sentence
# Accepted 2026-10-27T10:13:35+05:30. AI-assisted practice solution.
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
