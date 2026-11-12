# LeetCode 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Accepted as Suryakant_16 on 2026-11-12 13:46:10 IST (115/115 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        def dfs(node, remaining, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining:
                result.append(list(path))
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return result
