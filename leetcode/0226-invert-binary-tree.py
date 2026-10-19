# LeetCode 226. Invert Binary Tree
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 23:18 IST
# Pattern: Recursively swap children.
# Complexity: O(n) time, O(h) stack.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
