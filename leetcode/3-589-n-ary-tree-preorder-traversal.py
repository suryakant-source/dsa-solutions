# LeetCode 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Accepted as Suryakant_16 on 2026-11-04 13:46:57 IST (39/39 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []

        def dfs(node):
            if not node:
                return
            out.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return out
