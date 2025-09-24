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


# 2024
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, index, visited):
            if (not (0 <= r < len(board) and 0 <= c < len(board[0]))) or (r, c) in visited or board[r][c] != word[index]:
                return
            
            # 1. block is in bound 2. block is never visited, 3. block maches word[index]
            if index == len(word)-1:
                return True
            else:
                visited.add((r,c))
                find = dfs(r, c+1, index+1, visited) or dfs(r, c-1, index+1, visited) or dfs(r+1, c, index+1, visited) or dfs(r-1, c, index+1, visited)
                visited.remove((r,c))
                return find

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False

            
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[k]:
                return False

            visited.add((i, j))
            found = (
                dfs(i+1, j, k+1, visited) or
                dfs(i-1, j, k+1, visited) or
                dfs(i, j+1, k+1, visited) or
                dfs(i, j-1, k+1, visited)
            )
            visited.remove((i, j))  # backtrack
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False


