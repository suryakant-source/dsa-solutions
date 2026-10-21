class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        rank = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (0, rank[x]) if x in rank else (1, x))
