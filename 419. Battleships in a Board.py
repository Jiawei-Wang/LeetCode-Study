class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if not 0 <= i < rows or not 0 <= j < cols or board[i][j] != "X":
                return

            board[i][j] = "1"

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i+x, j+y) 

        counter = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    counter += 1
                    dfs(row, col)
        return counter


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # 不需要dfs或者bfs，因为战舰拜访只能横着或者竖着，所以每次遇到新的元素，检查其左边和上面是否为同等值即可，如果都不是则一定是新的战舰
        total = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    flag = 1
                    if j > 0 and board[i][j-1] == 'X': flag = 0
                    if i > 0 and board[i-1][j] == 'X': flag = 0
                    total += flag
        return total