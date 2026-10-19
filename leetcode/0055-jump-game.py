# LeetCode 55. Jump Game
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 16:02 IST
# Pattern: Greedy farthest-reach scan.
# Complexity: O(n) time, O(1) space.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, v in enumerate(nums):
            if i > far: return False
            far = max(far, i + v)
        return True
