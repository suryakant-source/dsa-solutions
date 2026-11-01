# LeetCode 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# Accepted as Suryakant_16 on 2026-11-01 13:16:02 IST (41/41 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if low <= node.val <= high:
                ans += node.val
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
        return ans
