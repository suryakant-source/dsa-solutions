# LeetCode 611. Valid Triangle Number
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: sort + fix the largest side, two pointers on the rest. Time O(n^2), space O(1).
# - Triangle condition a+b>c is monotone once sorted, so a two-pointer sweep counts all valid (a,b) for each c in one pass.
# - When nums[a]+nums[b] > nums[c], every index between a and b also works with b: add b-a at once.
# - Total O(n^2) beats the O(n^3) triple loop and avoids duplicates without a set.

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for c in range(n - 1, 1, -1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        return count
