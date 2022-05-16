from collections import deque

# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) # 1 <= rows and cols <= 10 so no corner cases
        
        fresh_cnt = 0 # keep track of fresh oranges
        rotten = deque() # BFS queue for rotten oranges
        minutes_passed = 0 # keep track of minutes passed
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c)) # add the rotten orange coordinates to the queue
                elif grid[r][c] == 1:
                    fresh_cnt += 1 # update fresh oranges count
        
        while rotten and fresh_cnt > 0: # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1
            
            for i in range(len(rotten)): # process rotten oranges on the current level
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols: # ignore the cell if it is out of the grid boundary
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2: # ignore the cell if it is empty '0' or visited before '2'
                        continue
                        
                    fresh_cnt -= 1 # update the fresh oranges count
                    grid[xx][yy] = 2 # mark the current fresh orange as rotten
                    rotten.append((xx, yy)) # add the current rotten to the queue

        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1

    
"""
对答案的理解：
1. 基本的逻辑是每个循环将：1.时间+1，2.当前烂橘子的周边橘子设为烂橘子并放入queue
2. 使用一个fresh_cnt来满足（最后循环结束时如果有剩的新鲜橘子则返回-1）这个corner case

使用变量：
1. 一个变量储存新鲜橘子数量
2. 一个变量储存总用时
3. 一个变量储存待遍历的烂橘子

流程：
1. 先遍历list找到时间为0时的初始新鲜橘子数量和烂橘子地址
2. 进入循环：条件为烂橘子还未被全部检测完且还剩新鲜橘子
    1. 进入循环时时间+1
    2. 本次循环将烂橘子queue中所有个体的邻居进行检测
    3. 找出邻居中的新鲜橘子，将其放入queue中用于下一轮循环
    4. 再相应更新变量
"""