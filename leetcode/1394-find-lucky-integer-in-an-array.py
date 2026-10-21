class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = {}
        for x in arr:
            cnt[x] = cnt.get(x, 0) + 1
        best = -1
        for k, v in cnt.items():
            if k == v:
                best = max(best, k)
        return best
