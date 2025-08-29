class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n # height of the tree rooted at each element

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # check if we have enough cables
        cable_number = len(connections)
        if cable_number < n - 1:
            return -1

        # enough cables means a solution is guaranteed
        # then check how many moves is needed
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a,b)
        return len(set(uf.find(i) for i in range(n))) - 1 # number of groups - 1


# dfs
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        # create graph 
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                if not visited[cur]:
                    visited[cur] = True
                    stack.extend(graph[cur])
                    # list.extend(iterable) takes another iterable and adds each of its elements to the end
                    # list.append(iterable) treats the whole iterable as a single element

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count - 1


# bfs: switch from stack to queue
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

        count = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                count += 1
        return count - 1