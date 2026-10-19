# LeetCode 139. Word Break
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 19:37 IST
# Pattern: DP over prefixes with a word set.
# Complexity: O(n^2) time, O(n) space.

class Solution:
    def wordBreak(self, s, wordDict):
        words=set(wordDict)
        longest=max(map(len,words))
        dp=[True]+[False]*len(s)
        for i in range(1,len(s)+1):
            dp[i]=any(dp[j] and s[j:i] in words for j in range(max(0,i-longest),i))
        return dp[-1]
