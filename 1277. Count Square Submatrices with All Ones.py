# same as leetcode 221: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# in this question dp[i][j] = k can represent two things
# 1. biggest square with matrix[i][j] as bottom right corner
# 2. number of squares with matrix[i][j] as bottom right corner

# solution 1: use full size 2d array for dp

# solution 2: only use two rows for dp
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = defaultdict(int) # extra row on top with everything as 0
        res = 0
        
        for r in range(rows):
            cur_dp = defaultdict(int) # a new row for dp
            for c in range(cols):
                if matrix[r][c] == 1:
                    cur_dp[c] = 1 + min(dp[c], cur_dp[c-1], dp[c-1])
                    # all non-exist values in defaultdict are set to 0
                    # so no need to check boundary
                    res += cur_dp[c]
            dp = cur_dp
        return res


# solution 3: in place
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                # if matrix[i][j] == 0: then it stays 0
                # if matrix[i][j] == 1: then it becomes min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))
        # map(sum, matrix) apply sum() to each row 
        # if matrix = [[1, 2], [3, 4]], this gives: map(sum, matrix) → [3, 7]
        # sum() add all rows together