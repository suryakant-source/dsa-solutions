class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        stack = [(sr, sc)]
        image[sr][sc] = color
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == old:
                    image[nr][nc] = color
                    stack.append((nr, nc))
        return image
