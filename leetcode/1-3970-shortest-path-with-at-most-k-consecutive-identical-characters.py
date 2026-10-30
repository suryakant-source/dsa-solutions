# LeetCode 3970. Shortest Path With At Most K Consecutive Identical Characters
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
# Accepted as Suryakant_16 on 2026-10-30 07:28:00 IST (1001/1001 testcases)
# Practice solution written with AI assistance for daily DSA practice

import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            cost, u, l = heapq.heappop(pq)
            if cost > dist[u][l]:
                continue
            if u == n - 1:
                return cost
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    nl = l + 1
                    if nl > k:
                        continue
                else:
                    nl = 1
                nd = cost + w
                if nd < dist[v][nl]:
                    dist[v][nl] = nd
                    heapq.heappush(pq, (nd, v, nl))
        return -1
