# LeetCode 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 21:11 IST
# Pattern: DFS: 1 + max(left, right).
# Complexity: O(n) time, O(h) stack.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
