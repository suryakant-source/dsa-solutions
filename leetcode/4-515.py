# LeetCode 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Accepted as Suryakant_16 on 2026-11-13 16:46:03 IST (78/78 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        result = []
        level = [root] if root else []
        while level:
            result.append(max(node.val for node in level))
            nxt = []
            for node in level:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            level = nxt
        return result
