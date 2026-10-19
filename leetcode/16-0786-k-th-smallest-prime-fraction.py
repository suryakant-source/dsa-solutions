# LeetCode 786. K-th Smallest Prime Fraction
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: binary search on the answer (fraction value) + two-pointer count and best tracking. Time O(n log(1/precision)), space O(1).
# - For a value x, a forward two-pointer counts fractions arr[i]/arr[j] <= x in O(n).
# - Track the largest fraction seen <= x; as the search converges it lands exactly on the k-th fraction.
# - Prime, unique inputs mean no value ties, so the best tracker identifies a unique answer pair.

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        lo, hi = 0.0, 1.0
        ans = [0, 1]
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2
            cnt = 0
            best = 0.0
            bi, bj = 0, 1
            j = 0
            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                if j < i + 1:
                    j = i + 1
                cnt += n - j
                if j < n and arr[i] > best * arr[j]:
                    best = arr[i] / arr[j]
                    bi, bj = i, j
            if cnt >= k:
                ans = [arr[bi], arr[bj]]
                hi = mid
            else:
                lo = mid
        return ans
