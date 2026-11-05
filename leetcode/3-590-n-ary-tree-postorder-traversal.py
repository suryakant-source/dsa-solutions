# LeetCode 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Accepted as Suryakant_16 on 2026-11-05 13:40:46 IST (38/38 testcases)
# Practice solution written with AI assistance for daily DSA practice

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []
        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            out.append(node.val)
        dfs(root)
        return out
