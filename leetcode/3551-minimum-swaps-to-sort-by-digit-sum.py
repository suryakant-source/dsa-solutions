# LeetCode 3551. Minimum Swaps to Sort by Digit Sum
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 17, 2026 07:08 IST
# Pattern: Sort by (digit sum, value), then count cycle swaps to reach sorted order (POTD Oct 17).
# Complexity: O(n log n) time, O(n) space.

class Solution:
    def minSwaps(self, nums):
        order = sorted(range(len(nums)), key=lambda i: (sum(map(int, str(nums[i]))), nums[i]))
        seen = [False] * len(nums)
        answer = 0
        for i in range(len(nums)):
            length = 0
            while not seen[i]:
                seen[i] = True
                i = order[i]
                length += 1
            answer += max(0, length - 1)
        return answer
