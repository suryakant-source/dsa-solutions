class Solution:
    def arrayPairSum(self, nums):
        a = sorted(nums)
        return sum(a[i] for i in range(0, len(a), 2))
