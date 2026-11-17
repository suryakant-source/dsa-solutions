# LeetCode 2879. Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
# Accepted as Suryakant_16 on 2026-11-17 07:28:05 IST (558/558 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10 ** 9
        divs = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            divs[L] = [d for d in range(1, L) if L % d == 0]
        eq = [[False] * n for _ in range(n)]
        for i in range(n):
            si = s[i]
            row = eq[i]
            for j in range(i + 1, n):
                if si == s[j]:
                    row[j] = True
        cost = [[INF] * n for _ in range(n)]
        for L in range(2, n + 1):
            for l in range(0, n - L + 1):
                r = l + L - 1
                best = INF
                for d in divs[L]:
                    m = L // d
                    half = m // 2
                    tot = 0
                    for c in range(d):
                        base = l + c
                        for i in range(half):
                            if not eq[base + i * d][base + (m - 1 - i) * d]:
                                tot += 1
                    if tot < best:
                        best = tot
                        if best == 0:
                            break
                cost[l][r] = best
        f = [[INF] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            maxj = k if k < i // 2 else i // 2
            for j in range(1, maxj + 1):
                best = INF
                for p in range(j * 2 - 2, i - 1):
                    v = f[p][j - 1] + cost[p][i - 1]
                    if v < best:
                        best = v
                f[i][j] = best
        return f[n][k]
