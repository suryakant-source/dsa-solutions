# LeetCode 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Accepted as Suryakant_16 on 2026-11-11 16:37:44 IST (97/97 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')
        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            best = max(best, node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return best
