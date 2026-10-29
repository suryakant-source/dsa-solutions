# LeetCode 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Accepted as Suryakant_16 on 2026-10-29 10:21:47 IST (31/31 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node
        return build(0, len(nums) - 1)
