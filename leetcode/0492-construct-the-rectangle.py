class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w = int(area ** 0.5)
        while area % w:
            w -= 1
        return [area // w, w]
