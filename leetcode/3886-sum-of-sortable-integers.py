# LeetCode 3886. Sum Of Sortable Integers
# Difficulty: Hard
# Status: Accepted (Python3)
# Solved: Oct 20, 2026
# Pattern: For each divisor k of n, check every block is a rotation of a sorted run and block max <= next block min; prefix sums of descents.

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n - 1):
            pre[i + 1] = pre[i] + (nums[i] > nums[i + 1])
        pre[n] = pre[n - 1] if n > 1 else 0
        nxt = [n] * (n + 1)
        for i in range(n - 2, -1, -1):
            nxt[i] = i if nums[i] > nums[i + 1] else nxt[i + 1]
        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            prev = 0
            ok = True
            for s in range(0, n, k):
                e = s + k - 1
                d = pre[e] - pre[s]
                if d == 0:
                    lo, hi = nums[s], nums[e]
                elif d == 1 and nums[e] <= nums[s]:
                    j = nxt[s]
                    lo, hi = nums[j + 1], nums[j]
                else:
                    ok = False
                    break
                if lo < prev:
                    ok = False
                    break
                prev = hi
            if ok:
                ans += k
        return ans
