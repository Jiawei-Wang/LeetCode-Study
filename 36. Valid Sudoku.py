class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        暴力解：
        1. 检查每一行
        2. 检查每一列
        3. 检查每个3*3
        """
        for row in board:
            curr = set()
            for item in row:
                if item != '.' and item in curr:
                    return False
                curr.add(item)
        
        for column in range(9):
            curr = set()
            for row in range(9):
                if board[row][column] != '.' and board[row][column] in curr:
                    return False
                curr.add(board[row][column])
                
        for i in range(0, 7, 3):
            for j in range(0, 7, 3): # 9个3*3的起始点：
                curr = set()
                for row in range(3):
                    for column in range(3):
                        if board[i+row][j+column] != '.' and board[i+row][j+column] in curr:
                            return False
                        curr.add(board[i+row][j+column])
        return True




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(row):
            check = set()
            for char in board[row]:
                if char != ".":
                    if char in check:
                        return False
                    else:
                        check.add(char)
            return True

        def isValidColumn(col):
            check = set()
            for index in range(9):
                char = board[index][col]
                if char != ".":
                    if char in check:
                        return False
                    else:
                        check.add(char)
            return True

        def isValidBox(box):
            check = set()
            row, col = box[0], box[1]
            for i in range(row, row+3):
                for j in range(col, col+3):
                    char = board[i][j]
                    if char != ".":
                        if char in check:
                            return False
                        else:
                            check.add(char)
            return True

        for row in range(9):
            if not isValidRow(row): return False 
        for col in range(9):
            if not isValidColumn(col): return False 
        for box in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            if not isValidBox(box): return False 
        return True
        