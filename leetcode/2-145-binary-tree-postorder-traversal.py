# LeetCode 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Accepted as Suryakant_16 on 2026-11-05 10:36:47 IST (71/71 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                out.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return out[::-1]
