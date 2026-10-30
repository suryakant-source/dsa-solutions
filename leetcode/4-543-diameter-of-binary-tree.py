# LeetCode 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Accepted as Suryakant_16 on 2026-10-30 16:09:39 IST (106/106 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        best = 0
        height = {None: 0}
        stack = [(root, False)]
        while stack:
            node, processed = stack.pop()
            if not node:
                continue
            if processed:
                left = height[node.left]
                right = height[node.right]
                if left + right > best:
                    best = left + right
                height[node] = max(left, right) + 1
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return best
