class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [[0] * 3 for _ in range(2)] # row[id][r]: the current number of characters that player id places on row r
        col = [[0] * 3 for _ in range(2)]
        d1 = [0] * 2 # d1[id]: the current number of characters that player id places on main diagonal
        d2 = [0] * 2
        id = 0 # 0 for A, 1 for B
        for r, c in moves: # 默认第一步是A走棋
            row[id][r] += 1 # A在第r行的总棋子数 +1
            col[id][c] += 1 # A在第c列的总棋子数 +1
            d1[id] += r == c # 如果棋子落在对角线上则 +1
            d2[id] += r + c == 2 # 斜对角线 r + c = 2
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]): # 只要任意一行或者一列或者对角线有3个棋子则当前玩家获胜
                return 'AB'[id]
            id ^= 1 # 转换玩家id
        return 'Draw' if len(moves) == 9 else 'Pending'
    
"""
对题目的理解：主要难点在于每次更新棋盘后如何快速检测是否有胜者，遍历棋盘肯定不是好方法
对答案的理解：将胜负条件从"保留2d棋盘，每步后检测棋盘上是否有某行或者某列所有元素均相同"，
             转变为"共8个可能解，保留玩家在可能解上的进度，若任一被满足则可知胜者"
"""