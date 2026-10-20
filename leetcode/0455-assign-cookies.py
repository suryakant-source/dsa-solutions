class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for x in s:
            if i < len(g) and g[i] <= x:
                i += 1
        return i
