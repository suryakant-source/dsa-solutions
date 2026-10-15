class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for left in range(len(nums)):
            seen = set()
            for right in range(left, len(nums)):
                seen.add(nums[right])
                total += len(seen) * len(seen)
        return total
