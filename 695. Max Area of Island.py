# bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        for row in range(rows):
            for col in range(cols): # go through all nodes
        
                if grid[row][col] == 1: # when we find an island
                    grid[row][col] = -1 # mark it
                    queue = deque([(row, col)]) # start BFS
                    area = 0
                    
                    while queue:
                        current_row, current_col = queue.popleft()
                        if grid[current_row][current_col] == -1: # if the part is marked
                            area += 1
                            grid[current_row][current_col] = 0  # erase it
                            
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # Explore neighbors
                            new_row, new_col = current_row + dx, current_col + dy
                            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1: # if neighbor is also part of island
                                grid[new_row][new_col] = -1
                                queue.append((new_row, new_col))
                                
                    max_area = max(max_area, area) # update answer every time when we finish an island
        
        return max_area
        
"""
to prevent putting a part into queue twice or more times, we need to temporarily mark it as -1, then turn it into 0
"""


# DFS iterative: change queue to stack
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def explore_island(row, col):
            area = 0
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    grid[r][c] = 0  # Mark visited
                    area += 1
                    stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = explore_island(row, col)
                    max_area = max(max_area, area)

        return max_area


# DFS recursive
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()

        def area(r, c): 
            # node is not legit
            # it must be (inside grid AND not visited AND part of island) to be counted
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0 

            # node is legit
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) + 
                    area(r, c-1) + area(r, c+1)) # return the area of the island that this part belongs to 

        # 学习是用两个for的用法，遍历2d list中所有点，返回(值最大)的那个点的值
        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

