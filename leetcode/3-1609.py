# LeetCode 1609. Even Odd Tree
# https://leetcode.com/problems/even-odd-tree/
# Accepted as Suryakant_16 on 2026-11-15 13:38:13 IST (107/107 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        level = [root]
        depth = 0
        while level:
            for i, node in enumerate(level):
                v = node.val
                if depth % 2 == 0:
                    if v % 2 == 0:
                        return False
                    if i > 0 and v <= level[i - 1].val:
                        return False
                else:
                    if v % 2 == 1:
                        return False
                    if i > 0 and v >= level[i - 1].val:
                        return False
            nxt = []
            for node in level:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            level = nxt
            depth += 1
        return True
