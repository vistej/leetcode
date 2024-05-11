class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        t = image[sr][sc]
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr - 1][sc] == t:
            image = self.floodFill(image, sr-1, sc, color)

        if sr + 1 < len(image) and image[sr + 1][sc] == t:
            image = self.floodFill(image, sr+1, sc, color)

        if sc - 1 >= 0 and image[sr][sc - 1] == t:
            image = self.floodFill(image, sr, sc-1, color)

        if sc + 1 < len(image[0]) and image[sr][sc + 1] == t:
            image = self.floodFill(image, sr, sc+1, color)

        return image