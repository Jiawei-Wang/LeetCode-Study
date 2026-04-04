# we only need sum not path
# modify grid in place to store current minimum sum
# for gird[i][j]: minimum sum = minimum sum on row i-1 that is not col j
# imagine minimum sum on row i-1 is k, on col j
# then for everyone on row i, except col j, they all take k
# and j takes the second smallest sum from row i-1
# so for each row, we need to keep track of smallest and second smallest sum
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0] # input is an n by n grid

        # Tracking variables for the PREVIOUS row
        prev_min1 = 0
        prev_min2 = 0
        prev_idx1 = -1 # Index of the absolute minimum

        for i in range(n):
            curr_min1 = float("inf")
            curr_min2 = float("inf")
            curr_idx1 = -1

            for j in range(n):
                # Step 1: Calculate the path sum for this cell
                # If current column is the same as previous row's min index, use second min
                if j == prev_idx1:
                    val = grid[i][j] + prev_min2
                else:
                    val = grid[i][j] + prev_min1
                
                # Step 2: Update the current row's min1 and min2
                if val < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = val
                    curr_idx1 = j
                elif val < curr_min2:
                    curr_min2 = val
            
            # Step 3: Shift current row stats to prev for next iteration
            prev_min1, prev_min2, prev_idx1 = curr_min1, curr_min2, curr_idx1
        
        return prev_min1 



