class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        top = sorted(set(nums), reverse=True)
        return top[2] if len(top) >= 3 else top[0]
