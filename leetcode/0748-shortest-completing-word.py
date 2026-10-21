class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        need = {}
        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1
        best = None
        for w in words:
            ok = True
            for ch, k in need.items():
                if w.count(ch) < k:
                    ok = False
                    break
            if ok and (best is None or len(w) < len(best)):
                best = w
        return best
