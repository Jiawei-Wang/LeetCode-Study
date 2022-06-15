class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 开头被堵
        if obstacleGrid[0][0]:
            return 0
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        # 只有一行或者一列
        if row == 1:
            return 0 if max(obstacleGrid[0]) else 1
        if col == 1:
            return 0 if max(x[0] for x in obstacleGrid) else 1
        
        dp = [[0] * col for i in range(row)]
        dp[0][0] = 1 
        
        # 第一列
        for i in range(1, row):
            if dp[i-1][0] and not obstacleGrid[i][0]:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        
        # 第一行
        for j in range(1, col):
            if dp[0][j-1] and not obstacleGrid[0][j]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        
        # 其他所有格子
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
                    
        return dp[-1][-1]