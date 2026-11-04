# LeetCode 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Accepted as Suryakant_16 on 2026-11-04 16:56:32 IST (71/71 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> List[int]:
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            out.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return out
