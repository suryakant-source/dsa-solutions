# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Accepted as Suryakant_16 on 2026-11-10 13:39:27 IST (203/203 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.i = 0
        def build(lo, hi):
            if lo > hi:
                return None
            val = preorder[self.i]
            self.i += 1
            node = TreeNode(val)
            mid = pos[val]
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node
        return build(0, len(inorder) - 1)
