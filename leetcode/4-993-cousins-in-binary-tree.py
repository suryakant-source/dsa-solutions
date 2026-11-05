# LeetCode 993. Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/
# Accepted as Suryakant_16 on 2026-11-05 16:56:44 IST (105/105 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q = deque([(root, None, 0)])
        info = {}
        while q:
            node, parent, depth = q.popleft()
            if node.val == x or node.val == y:
                info[node.val] = (parent, depth)
            if node.left:
                q.append((node.left, node, depth + 1))
            if node.right:
                q.append((node.right, node, depth + 1))
        return info[x][1] == info[y][1] and info[x][0] is not info[y][0]
