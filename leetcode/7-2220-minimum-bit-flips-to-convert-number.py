# 2220. Minimum Bit Flips to Convert Number
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/submissions/2182254631/
from typing import List

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

