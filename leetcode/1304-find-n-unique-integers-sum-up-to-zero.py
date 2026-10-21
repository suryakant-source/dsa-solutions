class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = list(range(1, n // 2 + 1)) + [-x for x in range(1, n // 2 + 1)]
        if n % 2:
            res.append(0)
        return res
