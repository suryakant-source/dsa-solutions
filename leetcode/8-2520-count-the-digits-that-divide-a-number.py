# 2520. Count the Digits That Divide a Number
# Accepted 2026-10-26 | AI-assisted practice
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/submissions/2182355658/
from typing import List

class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(d) == 0 for d in str(num))

