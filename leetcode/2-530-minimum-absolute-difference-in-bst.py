# LeetCode 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Accepted as Suryakant_16 on 2026-11-03 09:36:35 IST (190/190 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        prev = None
        best = float('inf')

        def inorder(node):
            nonlocal prev, best
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return best
