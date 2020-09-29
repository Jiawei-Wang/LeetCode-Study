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
