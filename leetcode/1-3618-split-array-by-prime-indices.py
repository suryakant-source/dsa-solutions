# 3618. Split Array by Prime Indices (Medium)
# Accepted: 2026-10-26 | AI-assisted practice
# Approach: Sieve of Eratosthenes, then signed sum
# Complexity: O(n log log n) time, O(n) space
# Submission: https://leetcode.com/problems/split-array-by-prime-indices/submissions/2181860931/

from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prime = [True] * n
        prime[0] = False
        if n > 1:
            prime[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if prime[p]:
                for j in range(p * p, n, p):
                    prime[j] = False
        return abs(sum(x if prime[i] else -x for i, x in enumerate(nums)))
