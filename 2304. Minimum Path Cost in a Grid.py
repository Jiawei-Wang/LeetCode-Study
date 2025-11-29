class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        last_cost = grid[-1][:] 

        for row in range(rows - 2, -1, -1): # start from 2nd last row
            current_cost = []
            for col in range(cols):
                cell = grid[row][col]
                costs = moveCost[cell]
                cost = grid[row][col] + min(x + y for x, y in zip(last_cost, costs))
                current_cost.append(cost)
            last_cost = current_cost
        
        return min(last_cost)
