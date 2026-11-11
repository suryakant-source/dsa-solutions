# LeetCode 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Accepted as Suryakant_16 on 2026-11-08 10:42:04 IST (33/33 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        out = []
        if not root:
            return out
        q = deque([root])
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                level.reverse()
            out.append(level)
            left_to_right = not left_to_right
        return out
