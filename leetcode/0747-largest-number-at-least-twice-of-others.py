class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        big = max(nums)
        idx = nums.index(big)
        for i, x in enumerate(nums):
            if i != idx and 2 * x > big:
                return -1
        return idx
