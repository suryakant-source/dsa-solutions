# LeetCode 367. Valid Perfect Square
# Difficulty: Easy
# Status: Accepted (Python3)
# Pattern: Binary search the integer square root; also pure math variant.
# Complexity: O(log n) time, O(1) space.

class Solution:
    def isPerfectSquare(self, num):
        l,r=1,num
        while l<=r:
            m=(l+r)//2
            if m*m==num: return True
            if m*m<num: l=m+1
            else: r=m-1
        return False
