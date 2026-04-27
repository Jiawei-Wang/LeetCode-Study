class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = [num for row in grid for num in row] # turn into 1d
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)

        l = l[-k:] + l[:-k]  # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # 1d to 2d