# LeetCode 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# Accepted as Suryakant_16 on 2026-10-31 13:23:55 IST (100/100 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        total = 0
        stack = [(root, False)]
        while stack:
            node, is_left = stack.pop()
            if not node:
                continue
            if is_left and not node.left and not node.right:
                total += node.val
            stack.append((node.left, True))
            stack.append((node.right, False))
        return total
