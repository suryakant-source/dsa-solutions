import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for v in nums:
            heapq.heappush(h, v)
            if len(h) > k: heapq.heappop(h)
        return h[0]
