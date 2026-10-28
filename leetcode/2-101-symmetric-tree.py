# LeetCode 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Accepted on LeetCode as Suryakant_16 on 2026-10-28 10:01 IST (201/201 testcases passed)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def mirror(a, b):
            if not a or not b:
                return a is b
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
        return mirror(root, root)
