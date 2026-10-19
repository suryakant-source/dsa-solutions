# LeetCode 74. Search a 2D Matrix
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Treat the 2D matrix as one sorted array; map mid to (row, col).
# Complexity: O(log(mn)) time, O(1) space.

class Solution:
    def searchMatrix(self, matrix, target):
        cols=len(matrix[0])
        l,r=0,len(matrix)*cols-1
        while l<=r:
            m=(l+r)//2
            x=matrix[m//cols][m%cols]
            if x==target: return True
            if x<target: l=m+1
            else: r=m-1
        return False
