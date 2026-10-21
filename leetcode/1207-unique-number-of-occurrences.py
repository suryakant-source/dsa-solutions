class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cnt = {}
        for x in arr:
            cnt[x] = cnt.get(x, 0) + 1
        return len(set(cnt.values())) == len(cnt)
