# LeetCode 867. Transpose Matrix
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: Transpose: result[j][i] = matrix[i][j].
# Complexity: O(mn) time, O(mn) output.

class Solution:
    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]
