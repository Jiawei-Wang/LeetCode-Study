class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        res = float("inf")
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for neighbor, distance in graph[node].items():
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                res = min(res, distance)
                
        return res