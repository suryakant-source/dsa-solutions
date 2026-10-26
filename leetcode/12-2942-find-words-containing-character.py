# 2942. Find Words Containing Character
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/find-words-containing-character/submissions/2182051895/
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

