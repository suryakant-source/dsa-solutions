# LeetCode 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted as Suryakant_16 on 2026-11-15 10:40:18 IST (63/63 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            count = 1 if node.val >= max_so_far else 0
            m = max(max_so_far, node.val)
            return count + dfs(node.left, m) + dfs(node.right, m)
        return dfs(root, root.val)
