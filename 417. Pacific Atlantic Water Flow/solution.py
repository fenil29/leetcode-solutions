class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)
        result = []
        POReachable = [[False for x in range(width)] for y in range(height)]
        AOReachable = [[False for x in range(width)] for y in range(height)]
        for i in range(width):
            self.explore(POReachable, heights, width,
                         height, 0, i, -float("inf"))
            self.explore(AOReachable, heights, width,
                         height, height-1, i, -float("inf"))
        for i in range(height):
            self.explore(POReachable, heights, width,
                         height, i, 0, -float("inf"))
            self.explore(AOReachable, heights, width,
                         height, i, width-1, -float("inf"))
        for i in range(height):
            for j in range(width):
                if(POReachable[i][j] and AOReachable[i][j]):
                    result.append([i, j])
        return result

    def explore(self, POReachable, heights, width, height, i, j, currentHeight):
        if i < 0 or j < 0 or j >= width or i >= height or POReachable[i][j] == True or heights[i][j] < currentHeight:
            return
        POReachable[i][j] = True
        self.explore(POReachable, heights, width,
                     height, i+1, j, heights[i][j])
        self.explore(POReachable, heights, width,
                     height, i-1, j, heights[i][j])
        self.explore(POReachable, heights, width,
                     height, i, j+1, heights[i][j])
        self.explore(POReachable, heights, width,
                     height, i, j-1, heights[i][j])
