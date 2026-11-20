# LeetCode 38. Count and Say
# https://leetcode.com/problems/count-and-say/
# Accepted as Suryakant_16 on 2026-11-20 16:35:45 IST (30/30 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            out = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                out.append(str(j - i) + s[i])
                i = j
            s = "".join(out)
        return s
