# LeetCode 199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted as Suryakant_16 on 2026-11-08 13:47:51 IST (217/217 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(out):
                out.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return out
