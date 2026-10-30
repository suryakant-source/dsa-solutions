# LeetCode 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# Accepted as Suryakant_16 on 2026-10-30 10:22:39 IST (228/228 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return height(root) != -1
