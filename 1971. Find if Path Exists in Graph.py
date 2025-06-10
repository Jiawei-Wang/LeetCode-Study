# bfs
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build graph (in the form of hashmap)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # use a queue to start from source
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        
        # each step visit neighbors
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        # still can't get to destination after finishing all steps
        return False


# dfs
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # same graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # change queue to stack
        visited = [False] * n
        stack = [start]
        visited[start] = True
        
        # also same logic, just popping from right instead of left
        while stack:
            top = stack.pop()
            if top == end:
                return True
            for neighbor in graph[top]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        return False
    

# union find 
class Solution:
    def __init__(self):
        self.parent = [] # index is the node, value is the node's parent node

    def findParent(self, node: int) -> int:
        # if we already have a non-self parent, we go down the trail and find the ultimate parent
        if self.parent[node] != node: 
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node] # return the ultimate parent or self

    def makeSameGroup(self, u: int, v: int):
        pu = self.findParent(u)
        pv = self.findParent(v)
        self.parent[pu] = pv # put two nodes in the same group by marking one as parent

    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        self.parent = list(range(n)) # everyone starts as its own parent

        for u, v in edges:
            self.makeSameGroup(u, v) # build the group(s)

        return self.findParent(start) == self.findParent(end) # check if start and end share same ultimate parent
