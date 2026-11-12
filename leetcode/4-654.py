# LeetCode 654. Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/
# Accepted as Suryakant_16 on 2026-11-12 16:46:17 IST (107/107 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None
        i = nums.index(max(nums))
        node = TreeNode(nums[i])
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node
