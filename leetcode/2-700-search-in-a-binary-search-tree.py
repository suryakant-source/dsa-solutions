# LeetCode 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Accepted as Suryakant_16 on 2026-11-01 10:24:31 IST (36/36 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = root
        while node:
            if node.val == val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return None
