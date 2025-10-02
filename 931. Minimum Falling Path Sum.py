class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        for i in range(1, length):
            for j in range(length):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][0], matrix[i-1][1])
                elif j == length - 1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
            
        return min(matrix[-1])