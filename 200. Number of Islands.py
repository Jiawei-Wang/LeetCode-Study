# 读题第一想法：遍历2D list，如果遇到'1'，且该'1'并未被标记，则count+1并标记自身，同时寻找其四个邻居直到边缘

# 解法1: dfs helper
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # corner case
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果这个点在查找先前其他'1'的时候被recursion已遍历，则其现在为'#'，不会再被遍历
                # 如果还是'1'，说明一定是孤立的新岛
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        # 如果到达边界则返回
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
            
        # 标记经过的点
        grid[i][j] = '#'
        # 对其4个邻居进行recursion
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


# BFS with a queue
from collections import deque
class Solution:
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue) 
                    count += 1
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 


# 05-16-2022
# DFS recursive
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr = self.dfs(grid, i, j)
                    area = max(area, curr)
        return area
    
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        curr = 1
        for dr, dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i+ dr
            c = j + dc
            if 0<= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                curr += self.dfs(grid, r,c)
        return curr
    
"""
逻辑：
1. 遍历2d list，每找到一块岛，计算面积，最后取最大值
2. 计算面积：本体面积 + 下一层recursion的返回值，basecase = 1
"""


# DFS with stack
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # 遍历所有元素找到符合条件的新岛
                    curr = self.dfs(grid, i, j) # 计算新岛面积
                    area = max(area, curr)
        return area
    
    def dfs(self, grid, i, j):
        stack = deque([[i,j]]) # 使用双重括号来将list放入stack中，单重括号会将2个元素单独放入stack中
        grid[i][j] = 0 # 标记走过的区域
        curr = 1 # 新岛初始面积为1
        while stack:
            i, j = stack.pop()
            for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
                r = i + dr
                c = j + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]== 1:
                    grid[r][c]=0
                    stack.append([r,c])
                    curr += 1
        return curr


# BFS with queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    curr = self.bfs(grid, i, j) 
                    area = max(area, curr)
        return area
    
    def bfs(self, grid, i, j):
        queue = deque([[i,j]]) 
        grid[i][j] = 0 
        curr = 1 
        while queue:
            i, j = queue.popleft()
            for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
                r = i + dr
                c = j + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]== 1:
                    grid[r][c]=0
                    queue.append([r,c])
                    curr += 1
        return curr


# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= rowLength or col < 0 or col >= colLength or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        count = 0
        rowLength = len(grid)
        colLength = len(grid[0])
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
                    
        return count


# bfs
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                if r < 0 or r >= rowLength or c < 0 or c >= colLength or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                queue.append((r-1, c))
                queue.append((r+1, c))
                queue.append((r, c-1))
                queue.append((r, c+1))

        count = 0
        rowLength = len(grid)
        colLength = len(grid[0])
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
                    
        return count