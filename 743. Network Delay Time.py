"""
Dijkstra
1. we have a distance list for all nodes and start from node k
(assume k is the first node: [0, inf, inf, inf, inf, etc])
2. we update k's neighbors' distances using k's edges
3. we pick the neighbor with shortest distance
4. we update its neighbors' distances using its edges
5. repeat
6. if any node is not visited, return -1 else return maximum distance
"""
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # first we need to have an edge collection
        edge = defaultdict(list)
        # key: i, value: a list of tuples (j, k)
        # from i to j there is an edge with weight k
        for time in times:
            edge[time[0]].append((time[1], time[2]))

        # then we need to have several variables
        visited = [False] * n # no node is visited (index = 0 means node 1 (nodes are labelled from 1 to n))
        distance = [float("inf")] * n  # everyone to node k is of distance inf
        distance[k-1] = 0 # k to itself is of distance 0
        max_distance = 0
    
        # each step we need to find the next node to visit (the one with current shortest distance)   
        # so we need a heap  
        # heap is to store all current distances and their node:
        # (5, 2): current distance from k to 2 is 5 (maybe there will be something better)
        heap = [(0, k)]  
        
        # every step we pick the nearest neighbor    
        while heap:
            cur = heapq.heappop(heap)
            cur_dis = cur[0]
            cur_node = cur[1]
            
            # Dijkstra only visits each node once 
            if visited[cur_node-1]:
                continue
            visited[cur_node-1] = True
            
            # now we update distance list using cur_node's edges
            for nei, nei_dis in edge[cur_node]:
                if not visited[nei-1]:
                    total_dis = cur_dis + nei_dis
                    if total_dis < distance[nei-1]: # if we find a shorter distance between k and nei-1
                        distance[nei-1] = total_dis
                        heapq.heappush(heap, (total_dis, nei))
                        # old distance for nei (longer one) is still in the heap but it is behind new distance (shorter)
                        # for a node: there may be multiple distances in heap but only the shortest one is used

        for boo in visited:
            if not boo:
                return -1
        return max(distance)




