# LeetCode 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/
# Accepted as Suryakant_16 on 2026-11-02 13:26:55 IST (48/48 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def leaves(node, out):
            if not node:
                return
            if not node.left and not node.right:
                out.append(node.val)
                return
            leaves(node.left, out)
            leaves(node.right, out)

        a, b = [], []
        leaves(root1, a)
        leaves(root2, b)
        return a == b
