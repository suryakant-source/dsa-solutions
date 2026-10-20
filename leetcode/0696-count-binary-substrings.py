class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        cur = 1
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                total += min(prev, cur)
                prev = cur
                cur = 1
        return total + min(prev, cur)
