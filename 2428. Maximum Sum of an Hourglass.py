class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        for i, j in product(range(1, m-1), range(1,n-1)):

                sm = ( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                      + grid[i  ][j] + # <-- hourglass center
                       grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] )

                if sm > ans: ans = sm

        return ans