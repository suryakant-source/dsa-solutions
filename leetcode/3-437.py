# LeetCode 437. Path Sum III
https://leetcode.com/problems/path-sum-iii/
# Accepted as Suryakant_16 on 2026-11-09 13:36:03 IST (130/130 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        self.ans = 0
        def dfs(node, running):
            if not node:
                return
            running += node.val
            self.ans += counts[running - targetSum]
            counts[running] += 1
            dfs(node.left, running)
            dfs(node.right, running)
            counts[running] -= 1
        dfs(root, 0)
        return self.ans
