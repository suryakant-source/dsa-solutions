# LeetCode 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Accepted as Suryakant_16 on 2026-11-12 10:30:25 IST (108/108 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node, acc):
            if not node:
                return 0
            acc = acc * 10 + node.val
            if not node.left and not node.right:
                return acc
            return dfs(node.left, acc) + dfs(node.right, acc)
        return dfs(root, 0)
