# LeetCode 3420. Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Accepted as Suryakant_16 on 2026-11-13 07:30:19 IST (731/731 testcases)
# Practice solution written with AI assistance for daily DSA practice

from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        cost = 0
        r = n - 1
        ans = 0
        for left in range(n - 1, -1, -1):
            x = nums[left]
            cnt = 1
            while dq and dq[0][0] < x:
                v, c = dq.popleft()
                cost += (x - v) * c
                cnt += c
            if dq and dq[0][0] == x:
                dq[0][1] += cnt
            else:
                dq.appendleft([x, cnt])
            while cost > k:
                v, c = dq[-1]
                cost -= (v - nums[r])
                if c == 1:
                    dq.pop()
                else:
                    dq[-1][1] -= 1
                r -= 1
            ans += r - left + 1
        return ans
