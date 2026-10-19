# LeetCode 739. Daily Temperatures
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 17:25 IST
# Pattern: Monotonic decreasing stack of indices.
# Complexity: O(n) time, O(n) space.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
