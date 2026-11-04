# LeetCode 3505. Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
# Accepted as Suryakant_16 on 2026-11-04 07:29:43 IST (774/774 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        import heapq
        from collections import defaultdict

        n = len(nums)
        cost = [0] * (n - x + 1)
        lo = []  # max-heap via negated values, holds the median
        hi = []
        delayed = defaultdict(int)
        sumlo = sumhi = 0
        sizelo = sizehi = 0

        def prune(heap, sign):
            while heap and delayed[sign * heap[0]]:
                delayed[sign * heap[0]] -= 1
                heapq.heappop(heap)

        def rebalance():
            nonlocal sumlo, sumhi, sizelo, sizehi
            if sizelo > sizehi + 1:
                v = -heapq.heappop(lo)
                sumlo -= v
                sizelo -= 1
                heapq.heappush(hi, v)
                sumhi += v
                sizehi += 1
                prune(lo, -1)
            elif sizehi > sizelo:
                v = heapq.heappop(hi)
                sumhi -= v
                sizehi -= 1
                heapq.heappush(lo, -v)
                sumlo += v
                sizelo += 1
                prune(hi, 1)

        def add(v):
            nonlocal sumlo, sumhi, sizelo, sizehi
            if lo and v <= -lo[0]:
                heapq.heappush(lo, -v)
                sumlo += v
                sizelo += 1
            else:
                heapq.heappush(hi, v)
                sumhi += v
                sizehi += 1
            rebalance()

        def discard(v):
            nonlocal sumlo, sumhi, sizelo, sizehi
            delayed[v] += 1
            if lo and v <= -lo[0]:
                sumlo -= v
                sizelo -= 1
                if v == -lo[0]:
                    prune(lo, -1)
            else:
                sumhi -= v
                sizehi -= 1
                if hi and v == hi[0]:
                    prune(hi, 1)
            rebalance()

        for i, v in enumerate(nums):
            add(v)
            if i >= x:
                discard(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                cost[i - x + 1] = med * sizelo - sumlo + sumhi - med * sizehi

        INF = float("inf")
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x:
                    cand = prev[i - x] + cost[i - x]
                    if cand < cur[i]:
                        cur[i] = cand
            prev = cur
        return prev[n]
