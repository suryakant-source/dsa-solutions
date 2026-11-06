# LeetCode 2747. Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/
# Accepted as Suryakant_16 on 2026-11-06 07:25:58 IST (3129/3129 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        from collections import defaultdict
        logs.sort(key=lambda l: l[1])
        freq = defaultdict(int)
        active = 0
        left = 0
        right = 0
        m = len(logs)
        ans = [0] * len(queries)
        for i in sorted(range(len(queries)), key=lambda i: queries[i]):
            t = queries[i]
            while right < m and logs[right][1] <= t:
                s = logs[right][0]
                if freq[s] == 0:
                    active += 1
                freq[s] += 1
                right += 1
            while left < m and logs[left][1] < t - x:
                s = logs[left][0]
                freq[s] -= 1
                if freq[s] == 0:
                    active -= 1
                left += 1
            ans[i] = n - active
        return ans
