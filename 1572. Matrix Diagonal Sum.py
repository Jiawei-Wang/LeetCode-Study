class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        total = 0
        for i in range(length):
            total += mat[i][i] + mat[i][length-i-1]
        if length % 2:
            return total - mat[length//2][length//2]
        else:
            return total