# LCS：经典DP
"""
2024
understanding:
1. we need one more extra row and one more extra column to provide initial value
2. if text1[i] and text2[j] are not a match, sub problem becomes: 
finding the biggest value for either text1[i+1] and text2[j], or text1[i] and text2[j+1]
3. if we find a match for text1[i] and text2[j], sub problem becomes:
finding the beggest value for text1[i+1] and text2[j+1]
"""
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


# https://leetcode.com/problems/longest-common-subsequence/discuss/348884/C%2B%2B-with-picture-O(nm)
# 因为subsequence没有要求元素必须相连，所以使用2d dp即可，横纵坐标分别代表text1和text2
# 这里展示的是 space n*m 的解法，但也可以套用Unique Paths中的方法，将space优化到只用两列
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans = [[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    ans[i+1][j+1] = ans[i][j] + 1
                else:
                    ans[i+1][j+1] = max(ans[i][j+1], ans[i+1][j])
        
        return ans[len(text1)][len(text2)]
        

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]