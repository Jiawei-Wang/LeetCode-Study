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
