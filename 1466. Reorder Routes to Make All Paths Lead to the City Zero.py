class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build adjacency list: positive edge means original direction
        al = defaultdict(list)
        for a, b in connections:
            al[a].append(b)   # original edge: a -> b
            al[b].append(-a)  # reverse edge: b -> -a (indicates b <- a)

        visited = [False] * n

        def dfs(from_node: int) -> int:
            visited[from_node] = True
            change = 0
            for to in al[from_node]:
                next_node = abs(to)
                if not visited[next_node]:
                    # if to > 0 means the road is in the wrong direction
                    change += dfs(next_node) + (1 if to > 0 else 0)
            return change

        return dfs(0)
