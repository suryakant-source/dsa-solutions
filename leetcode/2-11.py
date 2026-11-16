# LeetCode 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted as Suryakant_16 on 2026-11-16 10:31:12 IST (65/65 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def maxArea(self, height: list[int]) -> int:
        lo, hi = 0, len(height) - 1
        best = 0
        while lo < hi:
            best = max(best, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return best
