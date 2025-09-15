# 1. it is not a binary tree, it's just a tree (undirected, connected graph with n nodes and n-1 edges)
# 2. but still it is always better to collect all apples in current subtree then move on, than revisiting it later
# so this question becomes: traverse the whole tree, if any node is in hasApple, calculate the cost
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # turn list of edges into adj list for fast lookup (no need to go through edges every time)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set() # hashset for dfs 

        def dfs(node): # traverse the whole tree
            if node in visited:
                return 0
            visited.add(node)
            cost = 0
            for child in adj[node]:
                cost += dfs(child)
            if cost > 0:
                return cost + 2
            return 2 if hasApple[node] else 0

        return max(dfs(0) - 2, 0)