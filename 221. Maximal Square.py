# 在一个只有0和1组成的2d list中找到所有只包含1的正方形中面积最大者的面积
# 举例：
# 1 1 0 
# 1 1 0
# 0 0 1
# 每个1自身是个面积为1的正方形，左上角有个2*2的，所以答案为4

# 暴力解：对于每个1，从最长边长开始往内缩减，第一个符合条件的正方形即为以此点为左上角形成的最大正方形
class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        def is_valid_sqaure(row, col, side):
            return all(all(M[i][j] == '1' for j in range(col, col+side)) for i in range(row, row+side))
        
        m, n = len(M), len(M[0])
        for side_len in range(min(m,n), 0, -1):
            for row in range(m - side_len + 1):
                for col in range(n - side_len + 1):
                    if is_valid_sqaure(row, col, side_len):
                        return side_len**2
        return 0


# Brute Force
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        # cols不一定存在所以要保证有rows才去算cols，防止越界
        cols = len(matrix[0]) if rows else 0
        # 当前最佳答案
        maxsqlen = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    sqlen = 1
                    flag = True
                    # 如果没越界且上一层所有元素都是1
                    while sqlen + i < rows and sqlen + j < cols and flag:
                        # 遍历新的row和新的column，找到是否有0
                        for k in range(j, sqlen+j+1):
                            if matrix[i+sqlen][k] == '0':
                                flag = False
                                break
                        for k in range(i, sqlen+i+1):
                            if matrix[k][j+sqlen] == '0':
                                flag = False
                                break
                        # 如果在遍历完后每个元素依旧都是1,则往下方和右方扩一层
                        if flag:
                            sqlen += 1
                    # 更新最佳答案
                    if maxsqlen < sqlen:
                        maxsqlen = sqlen

        return maxsqlen * maxsqlen


# DP: https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
    

"""
example 1: 
0 1 1
1 1 1
1 1 1
dp[1][1] = 1 # biggest square with matrix[1][1] as bottom right corner is 1
dp[2][1] = 2
dp[1][2] = 2
dp[2][2] = 2

example 2:
1 1 0
1 1 1 
1 1 1
dp[1][1] = 2
dp[2][1] = 2
dp[1][2] = 1
dp[2][2] = 2

dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # one extra row and one extra col for 0s
        # so index won't go out of bound for first row and first col
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        longest = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    longest = max(longest, dp[r+1][c+1])
        
        return longest * longest
        