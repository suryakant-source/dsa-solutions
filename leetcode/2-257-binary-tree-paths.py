# LeetCode 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# Accepted as Suryakant_16 on 2026-10-31 10:28:29 IST (209/209 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> List[str]:
        if not root:
            return []
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return paths
