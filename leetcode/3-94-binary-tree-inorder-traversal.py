# LeetCode 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Accepted on LeetCode as Suryakant_16 on 2026-10-28 14:10 IST (71/71 testcases passed)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        out, stack, cur = [], [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            out.append(cur.val)
            cur = cur.right
        return out
