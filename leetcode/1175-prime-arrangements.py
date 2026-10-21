class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        primes = sum(1 for x in range(2, n + 1) if all(x % d for d in range(2, int(x ** 0.5) + 1)))
        res = 1
        for i in range(1, primes + 1):
            res = res * i % mod
        for i in range(1, n - primes + 1):
            res = res * i % mod
        return res
