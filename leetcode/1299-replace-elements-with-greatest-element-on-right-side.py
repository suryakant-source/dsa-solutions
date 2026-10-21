class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        best = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], best = best, max(best, arr[i])
        return arr
