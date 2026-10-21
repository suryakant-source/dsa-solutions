class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for x in range(1, n + 1):
            s = sum(int(c) for c in str(x))
            groups[s] = groups.get(s, 0) + 1
        top = max(groups.values())
        return sum(1 for v in groups.values() if v == top)
