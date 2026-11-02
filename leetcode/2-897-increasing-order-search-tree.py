# LeetCode 897. Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/
# Accepted as Suryakant_16 on 2026-11-02 10:23:25 IST (38/38 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        dummy = TreeNode()
        tail = dummy

        def inorder(node):
            nonlocal tail
            if not node:
                return
            inorder(node.left)
            node.left = None
            tail.right = node
            tail = node
            inorder(node.right)

        inorder(root)
        return dummy.right
