class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        
        m = len(A)
        n = len(B)
        
        ans = 0
        
        dp = [[0]* n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i] != B[j]:
                    dp[i][j] = 0
                else:
                    if not i or not j:
                        dp[i][j] = 1
                    elif i and j:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(dp[i][j], ans)
        return ans