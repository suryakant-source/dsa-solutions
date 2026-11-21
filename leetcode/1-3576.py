# LeetCode 3576. Find Subtree Sizes After Changes
# https://leetcode.com/problems/find-subtree-sizes-after-changes/
# Accepted as Suryakant_16 on 2026-11-21 07:26:48 IST (632/632 testcases)
# Practice solution written with AI assistance for daily DSA practice

from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        newp = parent[:]
        stacks = [[] for _ in range(26)]
        order = []
        st = [(0, False)]
        while st:
            x, leaving = st.pop()
            c = ord(s[x]) - 97
            if leaving:
                stacks[c].pop()
                continue
            if x != 0 and stacks[c]:
                newp[x] = stacks[c][-1]
            stacks[c].append(x)
            order.append(x)
            st.append((x, True))
            for y in children[x]:
                st.append((y, False))
        ans = [1] * n
        for x in reversed(order):
            if x != 0:
                ans[newp[x]] += ans[x]
        return ans
