# grid是正方形2d list，每个元素代表高度
# time = n时，可以到达高度不高于n的元素
# 求从左上角走到右下角最短时间
# 读题思考：其实等价于找到所有路径中（路径中最大元素）最小的那个
# 尝试使用dp，到达一个元素的最低需求时间
# 1.元素本身最高     2.元素介于邻居之间      3.元素本身最低
#      5                    5                   5
#  6   10   8          6    7    8         6    4    8
#      9                    9                   9
# 选元素本身           选元素本身             选邻居中最低值
# 所以如果元素不为最低选元素，不然选最低邻居
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                # 开头
                if not i and not j:
                    continue
                # 对于介于中间的元素
                if 1 <= i < n-1 and 1<= j < n-1:
                    neighbor = [grid[i-1][j], grid[i][j], grid[i-1][j-1], grid[i+1][j+1]]
                # 对于最上一行(不需要考虑从右边回来的情况，因为从右边回来的路径，其接下来再前往右下角的路径必然经过已遍历的位置)
                if not i:
                    neighbor = [grid[i][j-1], grid[i+1][j]]
                # 对于最下一行（同理不需要考虑从右边回来的情况） 
                if i == n-1:
                    if not j:
                        neighbor = [grid[i-1][j]]
                    else:
                        neighbor = [grid[i-1][j], grid[i][j-1]]
                # 对于最左一行（不考虑从下面上来的情况）
                if not j:
                    neighbor = [grid[i-1][j], grid[i][j+1]]
                # 对于最右一行
                if j == n -1:
                    neighbor = [grid[i-1][j], grid[i][j-1]]
                
                    if grid[i][j] < min(neighbor):
                        grid[i][j] = min(neighbor)
                        
        return grid[n-1][n-1]
    
"""
上面答案是错误的，因为遍历是从上到下，从左到右，所以假设有从右边来的路径，元素就无法被正确更新
举例：
[[0,1,2,3,4],
[24,23,22,21,5],
[12,13,14,15,16],
[11,17,18,19,20],
[10,9,8,7,6]]
因为正确路径是从右边来，而算法遍历顺序是从左边来，所以最中间的元素14应该被更新为16，而此算法依旧会返回14
"""


# 依旧是自己写的答案：
# 1. 已知答案范围一定是在末尾元素的值，和所有元素的最大值之间
# 2. sort list，然后将这个范围内的所有值全部进行检查
# 3. 第一个（能让我们从开头走到结尾）的值即为答案
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # 先把元素sort一下
        newGrid = []
        for i in range(n):
            for j in range(n):
                newGrid.append(grid[i][j])
        newGrid.sort()
        
        # 检查当前位置是否可以到达终点
        def helper(value, i, j):
            if (i < 0 or i >= n) or (j < 0 or j >= n):
                return False
            
            if (i, j) in visited:
                return False
            visited.add((i,j))
            
            if grid[i][j] > value:
                return False
            
            if i == n - 1 and j == n-1:
                return True
            
            return helper(value, i-1, j) or helper(value, i+1, j) or helper(value, i, j-1) or helper(value, i, j+1)
        
        # 然后按顺序查看水位涨到某个元素时是否可以从起点走到终点
        for value in newGrid:
            visited = set()
            if value >= grid[n-1][n-1] and helper(value, 0, 0):
                return value


# 和上面相同逻辑的解法：针对排序后逐个检查的优化：二分查找，其他不变


# dijkstra（priority queue）
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        res = 0
        
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))
