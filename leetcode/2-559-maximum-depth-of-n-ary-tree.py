# LeetCode 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Accepted as Suryakant_16 on 2026-11-04 10:38:23 IST (38/38 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        best = 0
        for child in root.children:
            best = max(best, self.maxDepth(child))
        return best + 1
