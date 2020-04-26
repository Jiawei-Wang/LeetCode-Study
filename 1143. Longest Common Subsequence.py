# LCS：经典DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 使用从左上角向右下角步进的方法
        # 首先是一个2D list，加1是因为设定index = 0为空
        # dp[i][j]表示text1到i，text2到j为止，当前最长LCS
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                # 如果相同则加1,如果不同则保留当前最大值并前进
                # 学习将if后置的语法
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
        
