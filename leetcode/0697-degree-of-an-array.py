class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first = {}
        cnt = {}
        best = 0
        ans = len(nums)
        for i, x in enumerate(nums):
            first.setdefault(x, i)
            cnt[x] = cnt.get(x, 0) + 1
            length = i - first[x] + 1
            if cnt[x] > best or (cnt[x] == best and length < ans):
                best = cnt[x]
                ans = length
        return ans
