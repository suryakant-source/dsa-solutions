# 1832. Check if the Sentence Is Pangram
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/submissions/2181975378/
from typing import List

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

