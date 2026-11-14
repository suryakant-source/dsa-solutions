# LeetCode 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/
# Accepted as Suryakant_16 on 2026-11-14 10:33:46 IST (109/109 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        def dfs(node, d):
            if not node:
                return
            if d == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        dfs(root, 1)
        return root
