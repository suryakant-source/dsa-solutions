# LeetCode 951. Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Accepted as Suryakant_16 on 2026-11-15 16:33:53 IST (81/81 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if not root1 or not root2:
            return root1 is root2
        if root1.val != root2.val:
            return False
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return no_flip or flip
