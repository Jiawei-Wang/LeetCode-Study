# Dijkstra + DP
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # adj list
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n 
            dist[src] = 0
            ways = [0] * n # additional array where ways[i] is number of shortest path from src = 0 to dst = i
            ways[src] = 1
            minHeap = [(0, src)]  # dist, src
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: # if this path is worse 
                    continue  # ignore
                
                # dist[u] >= d: this path is equal or better
                for v, time in graph[u]:
                    if dist[v] > d + time: # found a better path
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time: # found an equal path
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)