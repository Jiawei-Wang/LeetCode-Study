# 在2d list中找到最长的单调递增路径（每个元素都必须比前一个要大），然后返回其长度
# 限制条件：list长宽至少为1，每个元素都为0或者正整数

# 对所有点进行dfs
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        def path(i, j, value, length):
            if (i< 0 or i >= row) or (j<0 or j>= col) or matrix[i][j] <= value:
                return length
            return max(path(i+1,j, matrix[i][j], length+1), path(i-1,j, matrix[i][j], length+1), \
                       path(i,j+1, matrix[i][j], length+1), path(i,j-1, matrix[i][j], length+1))
        
        for i in range(row):
            for j in range(col):
                cur = path(i,j, -1, 0)
                ans = max(ans, cur)
        return ans
    

# dfs + cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)] # initially the longest path starting from every node is 0 
        
        def dfs(i, j): # for a node

            if not dp[i][j]: # if we already know longest path starting from it, then we skip this node

                val = matrix[i][j]

                # for a new node, its longest starting path = itself + longest path starting from any of the 4 neighbors
                dp[i][j] = 1 + max( 
                    # for a neightbor: first it has to exist, then it must be bigger than node
                    # if both satisfy: we use neighbor's path, otherwise 0 
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)

            return dp[i][j] # return is needed so other dfs loops can use current return value for calculation

        return max(dfs(x, y) for x in range(M) for y in range(N))   