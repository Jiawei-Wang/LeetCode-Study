class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # 当前的路径
        
        def dfs(r, c, i): # r,c: 当前元素，i: word中的进度
            if i == len(word): # 已经走到word的尽头
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or # 越界
                word[i] != board[r][c] or (r, c) in path): # 字符不匹配/已经遍历过board上的此元素
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False