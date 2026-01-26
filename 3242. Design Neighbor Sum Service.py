class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.hashmap = dict()
        for r in range(self.row):
            for c in range(self.col):
                value = self.grid[r][c]
                self.hashmap[value] = (r, c)

    def adjacentSum(self, value: int) -> int:
        total = 0
        r, c = self.hashmap[value]
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + i < self.row and 0 <= c + j < self.col:
                total += self.grid[r+i][c+j]
        return total
        

    def diagonalSum(self, value: int) -> int:
        total = 0
        r, c = self.hashmap[value]
        for i, j in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
            if 0 <= r + i < self.row and 0 <= c + j < self.col:
                total += self.grid[r+i][c+j]
        return total
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)