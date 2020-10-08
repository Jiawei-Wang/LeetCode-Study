class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # 读题第一想法：如何获得三视图每个的面积
        # top的面积是非0元素的个数
        # front的面积是每row最大的元素之和
        # side的面积是每column最大的元素之和

        top = 0
        front = 0
        column_max = grid[0]
        for i in range(len(grid)):
            front += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    top += 1
                if grid[i][j] > column_max[j]:
                    column_max[j] = grid[i][j]
        return top+front+sum(column_max)        
