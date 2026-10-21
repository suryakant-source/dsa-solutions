class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        res = []
        for v, i in zip(nums, index):
            res.insert(i, v)
        return res
