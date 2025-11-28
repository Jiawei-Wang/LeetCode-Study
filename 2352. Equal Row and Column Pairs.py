class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_map = defaultdict(int)
        for row in grid:
            row_tuple = tuple(row)
            row_map[row_tuple] += 1
        
        col_map = defaultdict(int)
        for j in range(len(grid[0])):
            col_tuple = tuple([grid[i][j] for i in range(len(grid))])
            col_map[col_tuple] += 1
        
        answer = 0
        for key, value in row_map.items():
            if key in col_map:
                answer += value * col_map[key]
        return answer
        