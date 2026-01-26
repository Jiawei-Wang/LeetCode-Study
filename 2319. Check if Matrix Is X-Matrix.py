class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:        
        row = len(grid)
        col = len(grid[0])

        def is_diagonal(r, c):
            return r == c or r + c == row - 1

        for r in range(row):
            for c in range(col):
                if is_diagonal(r, c):
                    if grid[r][c] == 0:
                        return False
                else:
                    if grid[r][c] != 0:
                        return False

        return True    
        