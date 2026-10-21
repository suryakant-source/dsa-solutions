class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []
        for i, w in enumerate(words):
            if any(i != j and w in v for j, v in enumerate(words)):
                res.append(w)
        return res
