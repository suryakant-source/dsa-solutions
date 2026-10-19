# LeetCode 91. Decode Ways
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 19:30 IST
# Pattern: DP over one- and two-digit decodings, zero handling.
# Complexity: O(n) time, O(1) space.

class Solution:
    def numDecodings(self, s):
        a,b=1,int(s[0]!='0')
        for i in range(1,len(s)):
            current=b if s[i]!='0' else 0
            if 10<=int(s[i-1:i+1])<=26: current+=a
            a,b=b,current
        return b
