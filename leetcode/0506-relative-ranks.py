class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        order = sorted(range(len(score)), key=lambda i: -score[i])
        res = [""] * len(score)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, i in enumerate(order):
            res[i] = medals[rank] if rank < 3 else str(rank + 1)
        return res
