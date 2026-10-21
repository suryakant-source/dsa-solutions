class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        cur = 0
        low = 0
        for x in nums:
            cur += x
            low = min(low, cur)
        return 1 - low
