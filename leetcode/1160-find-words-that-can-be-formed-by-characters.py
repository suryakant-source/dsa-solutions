class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        have = {}
        for ch in chars:
            have[ch] = have.get(ch, 0) + 1
        total = 0
        for w in words:
            need = {}
            for ch in w:
                need[ch] = need.get(ch, 0) + 1
            if all(have.get(ch, 0) >= k for ch, k in need.items()):
                total += len(w)
        return total
