# LeetCode 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Accepted as Suryakant_16 on 2026-11-11 10:28:10 IST (34/34 testcases)
# Practice solution written with AI assistance for daily DSA practice

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levels = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels[::-1]
