class Solution:
    def findLHS(self, nums: list[int]) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        best = 0
        for x in cnt:
            if x + 1 in cnt:
                best = max(best, cnt[x] + cnt[x + 1])
        return best
