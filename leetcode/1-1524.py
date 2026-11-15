# LeetCode 1524. Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Accepted as Suryakant_16 on 2026-11-15 07:24:56 IST (151/151 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1
        prefix = 0
        ans = 0
        for x in arr:
            prefix ^= (x & 1)
            if prefix:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % MOD
