# LeetCode 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/
# Accepted as Suryakant_16 on 2026-10-31 15:58:19 IST (182/182 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if not root1:
            return root2
        if not root2:
            return root1
        stack = [(root1, root2)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 or not n2:
                continue
            n1.val += n2.val
            if not n1.left:
                n1.left = n2.left
            elif n2.left:
                stack.append((n1.left, n2.left))
            if not n1.right:
                n1.right = n2.right
            elif n2.right:
                stack.append((n1.right, n2.right))
        return root1
