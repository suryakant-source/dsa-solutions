# LeetCode 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Accepted as Suryakant_16 on 2026-11-02 16:38:59 IST (66/66 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> List[float]:
        result = []
        level = [root]
        while level:
            result.append(sum(n.val for n in level) / len(level))
            level = [child for n in level for child in (n.left, n.right) if child]
        return result
