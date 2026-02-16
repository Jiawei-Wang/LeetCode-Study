class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        top = row
        bot = -1
        lft = col
        rgt = -1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    top = min(top, r)
                    bot = max(bot, r)
                    lft = min(lft, c)
                    rgt = max(rgt, c)
        
        return (bot - top + 1) * (rgt - lft + 1)
