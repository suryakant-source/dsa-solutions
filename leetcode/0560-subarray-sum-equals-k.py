# LeetCode 560. Subarray Sum Equals K
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 16:32 IST
# Pattern: Prefix sums + hashmap of seen prefix counts.
# Complexity: O(n) time, O(n) space.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}; s = res = 0
        for v in nums:
            s += v
            res += cnt.get(s - k, 0)
            cnt[s] = cnt.get(s, 0) + 1
        return res
