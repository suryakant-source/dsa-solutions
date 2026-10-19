# LeetCode 1011. Capacity To Ship Packages Within D Days
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: Binary search on answer: min ship capacity; greedy day count check.
# Complexity: O(n log sum(weights)) time, O(1) space.

class Solution:
    def shipWithinDays(self, weights, days):
        l,r=max(weights),sum(weights)
        while l<r:
            m=(l+r)//2
            used,load=1,0
            for x in weights:
                if load+x>m: used+=1;load=0
                load+=x
            if used<=days: r=m
            else: l=m+1
        return l
