class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        for i, j in product(range(1, m-1), range(1,n-1)):

                sm = ( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                      + grid[i  ][j] + # <-- hourglass center
                       grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] )

                if sm > ans: ans = sm

        return ans


# brute force is optimized already
# but I just want to try sliding window
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Build prefix sum matrix (extra row and column)
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = (grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j])

        def row_sum(r, c1, c2):
            # Sum of elements in row r from col c1 to c2, inclusive
            return prefix[r+1][c2+1] - prefix[r+1][c1] - prefix[r][c2+1] + prefix[r][c1]

        max_sum = float('-inf')
        for i in range(m-2):       # top row of hourglass
            for j in range(n-2):   # left column of hourglass
                total = row_sum(i, j, j+2) + grid[i+1][j+1] + row_sum(i+2, j, j+2)
                max_sum = max(max_sum, total)

        return max_sum