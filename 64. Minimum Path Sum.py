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


# 06-15-2022
# 思考：到某个点的最低路径总权重 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*col for i in range(row)]
        
        dp[0][0] = grid[0][0]
        for j in range(1,col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]