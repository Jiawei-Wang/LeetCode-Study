class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        c = collections.defaultdict(list) # key: a node on the graph, value: tuples of all other nodes (distance, node)
        
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        # 初始化
        cnt = 1 # 遍历到第一个点
        ans = 0 # 此时总边长为0
        visited = [0] * n 
        heap = c[0] # heap中有0这个点在dictionary中的value，即所有tuple
        visited[0] = 1 # 第一个点被visited
        heapq.heapify(heap) 
        while heap:
            d, j = heapq.heappop(heap) # 先从距离0最近的邻居开始
            if not visited[j]: 
                visited[j], cnt, ans = 1, cnt+1, ans+d # 将邻居放入visited表，遍历过的node总数+1，且将两者距离加入总边长
                for record in c[j]: heapq.heappush(heap, record) # 将这个邻居的所有邻居信息放入表中
            if cnt >= n: break 
        return ans