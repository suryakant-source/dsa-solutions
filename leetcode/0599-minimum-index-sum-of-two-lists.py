class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        idx = {w: i for i, w in enumerate(list1)}
        best = None
        res = []
        for j, w in enumerate(list2):
            if w in idx:
                s = idx[w] + j
                if best is None or s < best:
                    best = s
                    res = [w]
                elif s == best:
                    res.append(w)
        return res
