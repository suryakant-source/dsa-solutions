class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []
        for w in words:
            low = set(w.lower())
            if any(low <= r for r in rows):
                res.append(w)
        return res
