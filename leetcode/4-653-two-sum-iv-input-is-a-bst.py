# LeetCode 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Accepted as Suryakant_16 on 2026-11-03 15:57:12 IST (423/423 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
