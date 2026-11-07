# LeetCode 1882. Process Tasks Using Servers
# https://leetcode.com/problems/process-tasks-using-servers/
# Accepted as Suryakant_16 on 2026-11-07 07:25:24 IST (37/37 testcases)
# Practice solution written with AI assistance for daily DSA practice

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        for t, task in enumerate(tasks):
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            if free:
                w, i = heapq.heappop(free)
                heapq.heappush(busy, (t + task, w, i))
                ans.append(i)
            else:
                f, w, i = heapq.heappop(busy)
                heapq.heappush(busy, (f + task, w, i))
                ans.append(i)
        return ans
