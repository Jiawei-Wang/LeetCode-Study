# two step brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        # handle corner case: target out of matrix range
        if target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False

        # now we know target is within the matrix range
        # first find the target row (we 100% will find an index)
        row_list = [matrix[i][0] for i in range(row)] # list of first element of each row
        low_row = 0
        high_row = row - 1
        while low_row < high_row:
            mid_row = low_row + (high_row - low_row)//2 # lower bound

            # handle corner case: we find target 
            if target == row_list[low_row] or target == row_list[high_row] or target == row_list[mid_row]:
                return True
            elif row_list[mid_row] > target: 
                high_row = mid_row
            else:
                low_row = mid_row
            
            if low_row == high_row - 1: # we find two protential rows
                if target > row_list[high_row]:
                    low_row = high_row 
                break 

        # now we know target is within low_rol 
        # second find the target col (we may not find an index)
        col_list = [matrix[low_row][j] for j in range(col)]
        low_col = 0
        high_col = col - 1
        while low_col < high_col:
            mid_col = low_col + (high_col - low_col)//2

            # handle corner case: we find target
            if target == col_list[low_col] or target == col_list[high_col] or target == col_list[mid_col]:
                return True
            elif col_list[mid_col] > target:
                high_col = mid_col
            else:
                low_col = mid_col
            
            if low_col == high_col - 1: # same as row, we have two protential cols
                if target == matrix[low_row][low_col] or target == matrix[low_row][high_col]:
                    return True
                return False

        return target == matrix[low_row][low_col] 


# change to 1D binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                array.append(matrix[i][j])

        length = len(array)
        low = 0
        high = length - 1
        
        while low < high:
            mid = low + (high-low)//2
            if array[mid] < target:
                low = mid + 1
            else:
                high = mid
        return array[low] == target


# O(1) extra space: search in place instead of making a new array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows*cols-1
        
        while start <= end: # when start = end, we still need to do calculation one more loop
            mid = end + (start - end) // 2
            if matrix[mid//cols][mid%cols] == target: 
                return True
            if matrix[mid//cols][mid%cols] < target:
                start = mid + 1
            else:
                end = mid -1
        return False