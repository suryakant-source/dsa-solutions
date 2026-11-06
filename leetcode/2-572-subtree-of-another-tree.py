# LeetCode 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
# Accepted as Suryakant_16 on 2026-11-06 10:44:58 IST (185/185 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)
        def dfs(node):
            if not node:
                return False
            return same(node, subRoot) or dfs(node.left) or dfs(node.right)
        return dfs(root)
