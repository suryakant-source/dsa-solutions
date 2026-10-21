class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cnt = {}
        total = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            total += cnt.get(key, 0)
            cnt[key] = cnt.get(key, 0) + 1
        return total
