# LeetCode 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted as Suryakant_16 on 2026-11-07 14:10:22 IST (86/86 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
        return valid(root, float('-inf'), float('inf'))
