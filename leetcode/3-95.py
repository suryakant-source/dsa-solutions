# LeetCode 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Accepted as Suryakant_16 on 2026-11-11 13:33:43 IST (8/8 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(lo, hi):
            if lo > hi:
                return [None]
            trees = []
            for val in range(lo, hi + 1):
                lefts = build(lo, val - 1)
                rights = build(val + 1, hi)
                for left in lefts:
                    for right in rights:
                        trees.append(TreeNode(val, left, right))
            return trees
        return build(1, n)
