class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DP经典题

        # iteration
        row = len(grid)
        column = len(grid[0])
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for j in range(1, column):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row):
            for j in range(1, column):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
