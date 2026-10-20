class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        total = 0
        odd = False
        for v in cnt.values():
            total += v - v % 2
            if v % 2:
                odd = True
        return total + (1 if odd else 0)
