# LeetCode 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Accepted as Suryakant_16 on 2026-11-14 13:41:02 IST (111/111 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        i = 0
        def build(bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return None
            val = preorder[i]
            i += 1
            node = TreeNode(val)
            node.left = build(val)
            node.right = build(bound)
            return node
        return build(float('inf'))
