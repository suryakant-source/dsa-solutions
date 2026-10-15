class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[__import__('math').comb(r, k) for k in range(r + 1)] for r in range(numRows)]
