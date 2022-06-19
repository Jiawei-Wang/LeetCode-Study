# 在一个rows * cols的2d list上以[rCenter, cCenter]为起点BFS所有点
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = []
        visited = set()
        visited.add((rCenter, cCenter))
        queue = deque()
        queue.append((rCenter, cCenter))
        
        def valid(index):
            if 0 <= index[0] < rows and 0 <= index[1] < cols:
                return True
            return False
        
        while queue:
            curr = queue.popleft()
            ans.append(list(curr))
            for neighbor in [(0,1), (0, -1), (1,0), (-1,0)]:
                new = (curr[0]+neighbor[0], curr[1]+neighbor[1])
                if new not in visited and valid(new):
                    queue.append(new)
                    visited.add(new)
        return ans


# 数学
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - rCenter) + abs(pj - cCenter)

        points = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(points, key=dist)