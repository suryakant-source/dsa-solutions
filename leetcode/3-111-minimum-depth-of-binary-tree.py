# LeetCode 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Accepted as Suryakant_16 on 2026-10-30 13:21:24 IST (53/53 testcases)
# Practice solution written with AI assistance for daily DSA practice

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
