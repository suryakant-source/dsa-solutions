class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = num < 0
        num = abs(num)
        res = []
        while num:
            res.append(str(num % 7))
            num //= 7
        return ("-" if neg else "") + "".join(reversed(res))
