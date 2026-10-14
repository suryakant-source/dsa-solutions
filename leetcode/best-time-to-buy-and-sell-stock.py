class Solution:
    def maxProfit(self, prices):
        low = prices[0]
        best = 0
        for p in prices:
            best = max(best, p-low)
            low = min(low, p)
        return best
