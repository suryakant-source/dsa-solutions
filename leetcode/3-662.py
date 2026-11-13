# LeetCode 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Accepted as Suryakant_16 on 2026-11-13 13:35:57 IST (117/117 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        best = 1
        level = [(root, 0)]
        while level:
            best = max(best, level[-1][1] - level[0][1] + 1)
            nxt = []
            for node, pos in level:
                if node.left:
                    nxt.append((node.left, pos * 2))
                if node.right:
                    nxt.append((node.right, pos * 2 + 1))
            level = nxt
        return best
