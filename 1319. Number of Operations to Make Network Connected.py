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