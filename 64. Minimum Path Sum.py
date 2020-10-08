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


        # recursion (超时)
        row = len(grid)
        column = len(grid[0])

        def dp(i,j):
            if i != 0 and j != 0:
                return grid[i][j]+ min(dp(i-1,j), dp(i,j-1))
            elif i == 0 and j == 0:
                return grid[0][0]
            elif i == 0:
                return grid[i][j]+ dp(i,j-1)
            elif j == 0:
                return grid[i][j] + dp(i-1,j)

        return dp(row-1,column-1)
