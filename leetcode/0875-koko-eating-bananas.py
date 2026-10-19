# LeetCode 875. Koko Eating Bananas
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Binary search on answer: min eating speed; check with ceil division sum.
# Complexity: O(n log max(piles)) time, O(1) space.

class Solution:
    def minEatingSpeed(self, piles, h):
        l,r=1,max(piles)
        while l<r:
            m=(l+r)//2
            if sum((x+m-1)//m for x in piles)<=h: r=m
            else: l=m+1
        return l
