class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)] 
        # dp[i][j] = k: the minimum path from triangle[0][0] to triangle[i][j] is k

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            right = triangle[i][i]
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(value for value in dp[n-1])