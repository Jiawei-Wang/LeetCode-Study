# space mn answer: make a copy, go through original, update the copy based on original
# space m+n answer: go through original, mark rows and cols that need to be all 0s, update the original after the loop

# space 1 answer: 使用第一行记录所有列是否为0，使用第一列记录所有行是否为0，额外一个格子用于记录matrix[0][0]中被两者重叠导致丢失的信息
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1 # 额外的格子
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0 # 记录下第一列是否应该为0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        
"""
对于解法的理解：
正常情况下每次遇到一个0，就将其对应行和列都设为0，此时的情况是，走到其他同行或者同列的格子时，不知道其原本是否为0
先把第一列剥离出来，就可以把其是否为0的信息储存起来，再利用其来储存每一行是否为0
而对于第一行而言，遍历时是最先经过的，所以当进入其他行时，再用第一行来储存每一列是否为0，就不会造成冲突
"""
        

# 2024
# we can use elements in first col to mark if one row should be all 0s
# then we will lose information about if first col should be all 0s
# if any row should be all 0s, there will be a 0 on the first col
# so we need an extra variable to hold first col information
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1 
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows): # we go through every row
            if matrix[i][0] == 0: # if any element in the first col is 0
                col0 = 0 # we use an extra variable to mark first col as 0
            # go through every other element in this row
            # we don't care about matrix[i][0] because:
            # 1. if it is 0: it will stay 0 (whole row is marked)
            # 2. if it is not 0: it only becomes 0 when another element on this row is 0
            for j in range(1, cols): 
                if matrix[i][j] == 0: # if any element (row i col j) is 0
                    # we use first element in this row to mark row i as 0, first element in this col to mark col j as 0
                    matrix[i][0] = matrix[0][j] = 0 
            # this works for (using first row to store col inforamtion) because:
            # we go into first row first matrix[0][j]
            # 1. if it is 0: it will stay 0 (whole col is marked)
            # 2. if it is not 0: it only becomes 0 when another element on this col is 0
                    
        # change the matrix based on marks
        # we have to go backwards (for example if matrix[0][0] is 0, going forward will make the whole matrix 0)
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1): # first col is ignored
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0: # check if this element in first col needs to be updated
                matrix[i][0] = 0