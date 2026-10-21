class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        return sum(1 for i in range(m) for j in range(n) if rows[i] ^ cols[j])
