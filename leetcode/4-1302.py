# LeetCode 1302. Deepest Leaves Sum
# https://leetcode.com/problems/deepest-leaves-sum/
# Accepted as Suryakant_16 on 2026-11-14 16:33:55 IST (39/39 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        level = [root]
        while level:
            nxt = []
            for node in level:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if not nxt:
                return sum(node.val for node in level)
            level = nxt
        return 0
