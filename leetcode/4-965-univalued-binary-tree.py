# LeetCode 965. Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/
# Accepted as Suryakant_16 on 2026-11-01 16:27:41 IST (72/72 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None, val: int) -> bool:
            if not node:
                return True
            return node.val == val and dfs(node.left, val) and dfs(node.right, val)
        return dfs(root, root.val)
