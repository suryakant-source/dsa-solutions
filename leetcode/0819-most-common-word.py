class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import re
        ban = set(banned)
        cnt = {}
        for w in re.findall(r"[a-z]+", paragraph.lower()):
            if w not in ban:
                cnt[w] = cnt.get(w, 0) + 1
        return max(cnt, key=cnt.get)
