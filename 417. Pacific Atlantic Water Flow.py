# brute force: DFS or BFS on every cell: time (N*M)^2

# 找出连接pacific ocean的所有元素，找出连接atlantic ocean的所有元素，返回重叠部分: time N*M
# 具体方法：从第一行出发，dfs/bfs找到每个元素对应的邻居中所有能抵达top的元素，同理，从最后一行，第一列，最后一列出发，找到对应元素
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        # find all neighbors that satisfy requirements and put them into set
        def dfs(r, c, visit, prevHeight): 
        # r,c: index of element from last recursion
        # visit: pac or atl as a set
        # prevHeight: value of the element from last recursion
            if ((r, c) in visit or # this element satifies requirements and is already in the set
               r < 0 or c < 0 or r == ROWS or c == COLS or # over boarder
               heights[r][c] < prevHeight): # height can't be smaller than previous one
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # dfs on top row, find all that can reach pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # dfs on bottom row, find all that can reach atlantic
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # dfs on first column, find all that can reach pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # dfs on last column, find all that can reach atlantic
        
        res = [x for x in pac.intersection(atl)] # setA.interseaction(setB) 返回两者共同元素
        return res