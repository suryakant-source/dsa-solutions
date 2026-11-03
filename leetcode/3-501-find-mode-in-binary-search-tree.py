# LeetCode 501. Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Accepted as Suryakant_16 on 2026-11-03 12:45:56 IST (24/24 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def findMode(self, root: TreeNode | None) -> List[int]:
        modes = []
        prev = None
        run = 0
        best = 0

        def inorder(node):
            nonlocal prev, run, best
            if not node:
                return
            inorder(node.left)
            run = run + 1 if node.val == prev else 1
            prev = node.val
            if run > best:
                best = run
                modes.clear()
                modes.append(node.val)
            elif run == best:
                modes.append(node.val)
            inorder(node.right)

        inorder(root)
        return modes
