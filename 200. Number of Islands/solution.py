class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    ans += 1
                    self.exploreIsland(grid, i, j, width, height)
        return ans

    def exploreIsland(self, grid, i, j, width, height):
        if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"
            self.exploreIsland(grid, i+1, j, width, height)
            self.exploreIsland(grid, i, j+1, width, height)
            self.exploreIsland(grid, i-1, j, width, height)
            self.exploreIsland(grid, i, j-1, width, height)
