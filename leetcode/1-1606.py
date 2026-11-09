# LeetCode 1606. Find Servers That Handled Most Number of Requests
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Accepted as Suryakant_16 on 2026-11-09 07:24:50 IST (108/108 testcases)
# Practice solution written with AI assistance for daily DSA practice

import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        busy = []
        counts = [0] * k
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, s = heapq.heappop(busy)
                free.add(s)
            if not free:
                continue
            j = free.bisect_left(i % k)
            if j == len(free):
                j = 0
            s = free[j]
            free.remove(s)
            counts[s] += 1
            heapq.heappush(busy, (start + duration, s))
        m = max(counts)
        return [i for i, c in enumerate(counts) if c == m]
