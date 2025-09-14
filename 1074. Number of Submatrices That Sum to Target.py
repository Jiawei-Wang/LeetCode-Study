# apply idea from leetcode 560
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # prefix sum for each row 
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1] # do this in space since we don't need the input matrix anymore
        
        res = 0
        # for all possible column pairs
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                c[0] += 1
                cur = 0
                # for each row, apply the same logic as leetcode 560
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res