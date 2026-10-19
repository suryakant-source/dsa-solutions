# LeetCode 1569. Number of Ways to Reorder Array to Get Same BST
# Difficulty: Hard
# Status: Accepted (Python3)
# Pattern: BST structure + combinatorics (counting interleavings). Time O(n^2) for Pascal's triangle, recursion O(n log n) work; space O(n^2) for the table.
# Interview recall:
# - The first element fixes the root; elements smaller than it keep their relative order in the left subtree, larger in the right - so only the interleavings of left and right sequences vary.
# - At each node the count is C(left_size + right_size, left_size) * ways(left) * ways(right); multiply down the tree, mod 1e9+7.
# - Subtract 1 at the end to exclude the original ordering; n up to 1000 needs a recursion-limit bump for degenerate (sorted) input.

import sys
sys.setrecursionlimit(10000)


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            l, r = len(left), len(right)
            return C[l + r][l] * ways(left) % MOD * ways(right) % MOD

        return (ways(nums) - 1) % MOD
