# LeetCode 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Accepted as Suryakant_16 on 2026-10-29 14:13:23 IST (118/118 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()
            if not node.left and not node.right and total == targetSum:
                return True
            if node.left:
                stack.append((node.left, total + node.left.val))
            if node.right:
                stack.append((node.right, total + node.right.val))
        return False
