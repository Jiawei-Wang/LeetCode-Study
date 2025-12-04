# 此题就是要求找出每行每列最大的元素，然后计算每个元素和它所在行和列最大元素之间的差距
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in list(zip(*grid))]
        # list(zip(*grid))：
        # *grid把grid变成row1, row2, row3, etc
        # zip把这些row的每个元素逐个加起来
        # 最后得到的就是每一列元素
        
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += min(max_row[i],max_col[j]) - grid[i][j]

        return result
    
    
    
    
    
    