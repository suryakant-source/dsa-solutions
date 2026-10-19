# LeetCode 2916. Subarrays Distinct Element Sum of Squares II
# Difficulty: Hard
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 09:31 IST
# Pattern: Sliding window over distinct counts, sum of squares.
# Complexity: O(n^2) time, O(n) space.

class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        b1, b2 = [0]*(n+2), [0]*(n+2)
        def add(bit, i, value):
            while i <= n:
                bit[i] += value
                i += i & -i
        def query(bit, i):
            total = 0
            while i:
                total += bit[i]
                i -= i & -i
            return total
        def prefix(i):
            return query(b1,i)*i-query(b2,i)
        last = {}
        ending = answer = 0
        mod = 1000000007
        for r,x in enumerate(nums,1):
            l = last.get(x,0)+1
            old = prefix(r)-prefix(l-1)
            ending = (ending+2*old+r-l+1) % mod
            answer = (answer+ending) % mod
            add(b1,l,1)
            add(b1,r+1,-1)
            add(b2,l,l-1)
            add(b2,r+1,-r)
            last[x] = r
        return answer
