class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) < len(digits):
            letters, digits = digits, letters
        res = []
        for i in range(len(letters)):
            res.append(letters[i])
            if i < len(digits):
                res.append(digits[i])
        return "".join(res)
