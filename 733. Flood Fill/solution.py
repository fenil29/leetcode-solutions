class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, ogColor: int = None) -> List[List[int]]:
        if ogColor == None:
            ogColor = image[sr][sc]
        width = len(image[0])
        height = len(image)
        if(sr < 0 or sc < 0 or sr >= height or sc >= width or image[sr][sc] == color or ogColor != image[sr][sc]):
            return image
        else:
            image[sr][sc] = color
            self.floodFill(image, sr-1, sc, color, ogColor)
            self.floodFill(image, sr, sc-1, color, ogColor)
            self.floodFill(image, sr+1, sc, color, ogColor)
            self.floodFill(image, sr, sc+1, color, ogColor)
        return image
