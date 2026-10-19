# LeetCode 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: staircase search from the top-right corner (both rows and columns sorted non-increasing).
# Time O(m + n), space O(1).
# Interview recall:
# - Start top-right: if a cell is negative, every cell below it in that column is negative too.
# - Add the whole column remainder, then step left; otherwise step down.
# - Each move discards a row or a column, so at most m+n steps.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row, col = 0, cols - 1
        count = 0
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1
        return count
