# LeetCode 3841. Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
# Accepted as Suryakant_16 on 2026-10-29 07:28:24 IST (1040/1040 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        LOG = max(1, n.bit_length())
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[0] * n for _ in range(LOG)]
        t = 0
        stack = [(0, 0, 0)]
        while stack:
            node, par, ci = stack[-1]
            if ci == 0:
                tin[node] = t
                t += 1
            if ci < len(g[node]):
                nb = g[node][ci]
                stack[-1] = (node, par, ci + 1)
                if nb != par:
                    depth[nb] = depth[node] + 1
                    up[0][nb] = node
                    stack.append((nb, node, 0))
            else:
                tout[node] = t - 1
                stack.pop()
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            k = 0
            while d:
                if d & 1:
                    u = up[k][u]
                d >>= 1
                k += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]
        size = n + 2
        bit = [0] * size
        def upd(i, d):
            i += 1
            while i < size:
                bit[i] ^= d
                i += i & -i
        def pref(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r
        val = [1 << (ord(c) - 97) for c in s]
        for v in range(n):
            upd(tin[v], val[v])
            upd(tout[v] + 1, val[v])
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                nb = 1 << (ord(parts[2]) - 97)
                d = val[u] ^ nb
                if d:
                    upd(tin[u], d)
                    upd(tout[u] + 1, d)
                    val[u] = nb
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                m = pref(tin[u]) ^ pref(tin[v]) ^ val[w]
                ans.append((m & (m - 1)) == 0)
        return ans
