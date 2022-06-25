# 学习Prim算法: 从一个出发点开始，每次从可选的edge中选择最短的那个，然后更新已遍历node的list以及可选edge的heap

# graph中每个元素为：第一个点，第二个点，两个点的edge的边长
# 下面这个例子最后的答案应该为：0连接2（4），2连接3（1），2连接4（3），3连接1（4），总边长为12
graph = [[0, 1, 7], [0, 2, 4], [1, 2, 5], [1, 3, 4], [2, 3, 1], [2, 4, 3], [3, 4, 6]]

import collections
import heapq

def mst(graph):
    # 第一步是创建dictionary
    distance = collections.defaultdict(list) # key: 一个node，value: 多个tuple，每个是 (到邻居点的距离，邻居点)
    for item in graph:
        distance[item[0]].append((item[2], item[1]))
        distance[item[1]].append((item[2], item[0]))
    
    # 第二步是用0这个node将状态初始化
    total_nodes = len(distance) # 图中总共有多少个node
    visited = [1] + [0] * (total_nodes-1) # 从0这个node开始，其他node此时还未被遍历
    count = 1 # 一共遍历了1个node
    heap = distance[0] # 把0的所有邻居放入heap中
    heapq.heapify(heap)
    
    totalWeight = 0
    
    while heap:
        edge, node = heapq.heappop(heap) # 将可选的边中权重最低的边pop
        if not visited[node]: # 如果对应的node已经被遍历过就继续pop
            visited[node] = 1
            count += 1
            totalWeight += edge
            for neighbor in distance[node]: # 将新遍历到的node的边放入heap
                heapq.heappush(heap, neighbor)
        if count >= total_nodes:
            break
    
    return totalWeight
    
print(mst(graph))