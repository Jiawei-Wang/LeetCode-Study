class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 0:
                return 0
            
            total = grid[r][c]
            grid[r][c] = 0
            
            return total + bfs(r+1, c) + bfs(r-1, c) + bfs(r, c+1) + bfs(r, c-1)
    
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    best = max(best, bfs(i, j))
        return best
