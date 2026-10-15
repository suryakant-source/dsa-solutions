class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = best = nums[0]
        for v in nums[1:]:
            c = (v, mx * v, mn * v)
            mx, mn = max(c), min(c)
            best = max(best, mx)
        return best
