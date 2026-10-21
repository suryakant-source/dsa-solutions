class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        res = []
        acc = 0
        for x in sorted(nums, reverse=True):
            res.append(x)
            acc += x
            if acc > total - acc:
                break
        return res
