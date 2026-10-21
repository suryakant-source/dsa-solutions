class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        res = 0
        for c in s:
            bal += 1 if c == "L" else -1
            if bal == 0:
                res += 1
        return res
