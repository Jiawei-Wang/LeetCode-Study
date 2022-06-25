# 学习Dijskstra：找到从出发点开始，到所有其他node的最短路径
# 每次取当前最近的一个新node，然后从此node开始再更新其他node
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

class Graph():
    # 假设input是：一共n个node（0~ n-1），然后full graph是一个n*n的2d list
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                  for row in range(vertices)]
    
    # 这个method只是用来打印答案而已
    def printSolution(self, dist):
        print("Distance of each node from Source")
        for node in range(self.V):
            print(node, ':', dist[node])

    # 找到下一个最近的node，这里使用的是遍历，但其实可以用heap来优化
    def minDistance(self, dist, sptSet):
        min = float('inf')
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        # 初始化：出发点的距离为0，其他node的距离为inf
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        # 然后遍历所有node，每一轮都尝试更新距离
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            # 使用当前正在访问的node来更新距离表
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                    dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

# example 
g = Graph(9) # 一共9个node
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], # 第0个node有两个edge，和第1个距离4，和第7个距离8
           [4, 0, 8, 0, 0, 0, 0, 11, 0], # 以此类推，第1个node有两个edge，和第0个距离4，和第7个距离11
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
g.dijkstra(0)