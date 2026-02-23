"""
translate visual movement into logic 
for a ball at grid[r][c]:
    1. if grid[r][c] == 1:
        the ball wants to move to right side
        it only moves if grid[r][c+1] == 1
        if grid[r][c+1] == -1, it gets stuck, if c+1 is out of bounds, it gets stuck
    2. same logic for grid[r][c] == -1:
        grid[r][c-1] needs to be -1 as well to allow it to pass
"""
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        dp = list(range(cols)) # Initially, each ball i is at column i
        
        for row in range(rows):
            new_dp = []

            # let curr_col be the column the ball is currently in at the current row
            for curr_col in dp:
                if curr_col == -1: # if a ball is stuck at current row
                    new_dp.append(-1) # then it will always be stuck 
                    continue
                
                direction = grid[row][curr_col]
                next_col = curr_col + direction
                
                # a ball can fall into next row only when it doesn't go out of bounds 
                # and neighbor column has same value
                if 0 <= next_col < cols and grid[row][next_col] == direction:
                    new_dp.append(next_col)
                else:
                    new_dp.append(-1)
            dp = new_dp
            
        return dp