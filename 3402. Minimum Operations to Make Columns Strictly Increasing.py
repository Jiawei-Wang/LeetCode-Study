class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        ops = 0
        for c in range(col):
            prev = grid[0][c]
            for r in range(1, row):
                curr = grid[r][c]
                if curr <= prev:
                    ops += prev + 1 - curr
                    prev += 1
                else:
                    prev = curr
        return ops
