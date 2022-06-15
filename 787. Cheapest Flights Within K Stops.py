# 06-12-2022
# 找最短路径，但是有额外要求：最多只能经过 k+1 个edge
# BFS/DFS：遍历adj list，当路径长度到达上限时停止
# Bellman Ford：核心依旧是DP
# Dijkstra/Priority Queue

# 学习Prim's Minimum Spanning Tree
# https://www.youtube.com/watch?v=cplfcGZmX7I&ab_channel=MichaelSambol
# 学习Bellman Ford
# https://www.youtube.com/watch?v=obWXjtg0L64&t=24s&ab_channel=MichaelSambol
# 学习Dijkstra
# https://www.youtube.com/watch?v=_lHSawdgXpI&ab_channel=MichaelSambol
# Bellman Ford和Dijkstra的区别
# https://stackoverflow.com/questions/19482317/bellman-ford-vs-dijkstra-under-what-circumstances-is-bellman-ford-better
# Prim和Dijkstra的区别：
# https://stackoverflow.com/questions/14144279/difference-between-prims-and-dijkstras-algorithms


# 解法1：Priority Queue
# 基本逻辑：从src开始，每次选择最近的一个点，然后更新它所有的邻居，直到找到答案或者步数被用完
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 使用defaultdict的意义在于：当key不存在的时候，会返回一个默认值，而非KeyError
        f = collections.defaultdict(dict)
        # a, b, p分别是edge的：起点，终点，权重
        for a, b, p in flights:
            # f最终结构是这样的：{a:{b:p}}，即每个起点，自己拥有一个独立的dict，其中键值对是终点：权重
            f[a][b] = p
        # 此时就把flights这个array转换成了dictionary

        # 初始化一个PQ
        heap = [(0, src, K + 1)]
        while heap:
            # heapq.heappop: remove and return the smallest element from heap
            # p, i, k分别是：到i这个点的总权重，i的下标，还剩可用步数（总共k次）
            # 比如起点：距离为0，下标为src，还剩k+1步可用
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                #对于f中i这个key，把它的value取出来（它的value是它所有邻居以及邻边的权重）
                for j in f[i]:
                    # 更新j这个点的信息
                    """
                    下面这句话是这道题针对dijkstra的改变：dijkstra在这里对比获得的新权重和原有权重，如果新的更低，则
                    覆盖原有权重，而这里不进行比较，直接heappush进去，然后在heappop时，可以保证得到的是j这个点的所有
                    符合步数要求的权重中最低的那一个
                    """
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

"""
对于整个程序的理解：
1. 算法部分是标准的dijkstra：每次取一个点，然后计算其邻居的总权重
2. 因为dijkstra每次取总权重最小的点，所以可以保证每个点只被遍历一次，而且遍历完成后一定可以获得最小值，无需再次更新
3. 针对这道题进行的修改是：记住已走步数，如果在k步内找到答案，返回，如果超过k步，则停止
4. 程序分成两个部分：
    1）先把array转换成dict，这样做的意义是可以快速找到某个点的所有邻居
    2）不停地把dict中的内容放入PQ中，直到找到答案或者k被用完（PQ每次弹出最小值元素，即为dijkstra算法中下一步要访问的点）
"""


# DFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.ans_dfs = float('inf')
        
        def dfs(Map, src, dst, k, cost):
            if k < 0:
                return 
            if src == dst:
                self.ans_dfs = cost # 不需要对比min，因为下面直接把高于当前cost的路径给略过了
                return 
            if src not in Map: # 走到死胡同
                return 
            for i in Map[src]:
                if cost + i[1] > self.ans_dfs:
                    continue
                dfs(Map, i[0], dst, k-1, cost+i[1]) # 前进到下一个点
        
        # key: src, value: [dst, weight]
        Map = collections.defaultdict(list)
        for i in flights:
            Map[i[0]] += [[i[1], i[2]]]
        dfs(Map, src, dst, k+1, 0) 
        
        return self.ans_dfs if self.ans_dfs != float('inf') else -1


# BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        Map = collections.defaultdict(list)
        for i in flights:
            Map[i[0]] += [[i[1], i[2]]]
        
        step = 0
        q = deque()
        q.append([src, 0])
        ans = float('inf')
        
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr[0] == dst:
                    ans = min(ans, curr[1])
                if curr[0] not in Map:
                    continue
                for f in Map[curr[0]]:
                    if curr[1] + f[1] > ans:
                        continue
                    q.append([f[0], curr[1]+f[1]])
            
            if step > k:
                break
            step += 1

        return ans if ans != float('inf') else -1


# Bellman Ford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0
        
        for i in range(k+1):
            temp = cost.copy()
            for f in flights:
                curr = f[0]
                next = f[1]
                price = f[2]
                
                if cost[curr] == float('inf'):
                    continue
                temp[next] = min(temp[next], cost[curr]+price)
            
            cost = temp
            
        return cost[dst] if cost[dst] != float('inf') else -1 