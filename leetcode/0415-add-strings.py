class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += ord(num1[i]) - 48
                i -= 1
            if j >= 0:
                s += ord(num2[j]) - 48
                j -= 1
            res.append(str(s % 10))
            carry = s // 10
        return "".join(reversed(res))
