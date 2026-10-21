class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        prod = 1
        for d in digits:
            prod *= d
        return prod - sum(digits)
