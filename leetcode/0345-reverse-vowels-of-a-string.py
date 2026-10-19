# LeetCode 345. Reverse Vowels Of A String
# Status: Accepted (Python3)
# Solved: Oct 20, 2026 01:30 IST

from collections import Counter, defaultdict

class Solution:
    def reverseVowels(self, s):
        a = list(s)
        vowels = set('aeiouAEIOU')
        l,r = 0,len(a)-1
        while l < r:
            if a[l] not in vowels: l += 1
            elif a[r] not in vowels: r -= 1
            else:
                a[l],a[r] = a[r],a[l]
                l += 1
                r -= 1
        return ''.join(a)
