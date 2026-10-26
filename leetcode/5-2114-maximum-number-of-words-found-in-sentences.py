# 2114. Maximum Number of Words Found in Sentences
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/submissions/2182166512/
from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(' ') + 1 for s in sentences)

