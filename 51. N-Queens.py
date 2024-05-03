"""
when location (x, y) is occupied, another location (i, j) is invalid when:
i == x or j == y (horizontal or vertical)
or 
i + j = x + y or i - j = x - y (diagonal)
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # we check row by row: put a queen on 0-th row
        # then on 1st row check what columns are available to put the next queen
        # repeat
        # so in this way we don't have to check i == x
        def dfs(locations, xy_dif, xy_sum):
            # locations: list of column indices of all existing queens
            # for example: [1, 3] means on 0-th row we put on 1st col, on 1st row we put on 3rd col
            # it serves two purposes:
            # 1. it will provide the information to draw return value matrix
            # 2. it will provide the information to check if j == y
            # xy_dif: list of all existing x-y
            # xy_sum: list of all existing x+y
            
            # we now enter a new row, there is no queen on this row, all previous rows have queens on them
            row = len(locations) # if we have 2 existing queens on board, then we are currently on 2rd row 

            # first we check if dfs can end
            if row == n: # we have entered the "row" below the last row on board
                result.append(locations)
                return 
            
            # if dfs doens't end now (current row is still not fulfilled)
            # we pick a column for the new queen
            for col in range(n):
                # 1. col cannot be as the same as any previous col
                # 2. row - col cannot be as the same as any previous x - y
                # 3. row + col cannot be as the same as any previous x + y
                if col not in locations and row-col not in xy_dif and row+col not in xy_sum: # we find an available col for this queen
                    dfs(locations+[col], xy_dif+[row-col], xy_sum+[row+col]) # update and go to next loop

        result = []
        dfs([],[],[])
        # there are multiple solutions in result
        # each solution has a list of column indices
        # so if n = 4, index = 1, the row should be ". Q . ." 
        return [["." * col + "Q" + "." * (n-col-1) for col in solution] for solution in result]