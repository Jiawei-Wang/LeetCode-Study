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

        