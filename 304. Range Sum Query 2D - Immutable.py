# 2d prefix sum 

# sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i-1][j-1]
# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.sums = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        
        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                self.sums[i][j] = (
                    matrix[i - 1][j - 1] +
                    self.sums[i - 1][j] +
                    self.sums[i][j - 1] -
                    self.sums[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sums[row2 + 1][col2 + 1] -
            self.sums[row2 + 1][col1] -
            self.sums[row1][col2 + 1] +
            self.sums[row1][col1]
        )

    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)