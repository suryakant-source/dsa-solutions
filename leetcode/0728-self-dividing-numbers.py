class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        for x in range(left, right + 1):
            y = x
            ok = True
            while y:
                d = y % 10
                if d == 0 or x % d:
                    ok = False
                    break
                y //= 10
            if ok:
                res.append(x)
        return res
