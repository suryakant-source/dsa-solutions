class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums); best = 0
        for v in s:
            if v - 1 not in s:
                e = v
                while e + 1 in s: e += 1
                best = max(best, e - v + 1)
        return best
