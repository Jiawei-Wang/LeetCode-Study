"""
input:
1. n nodes 
2. a list of edges
output: number of connected components in the graph

example: n = 5, edges = [[0,1], [1,2], [3,4]]
return 2
"""


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        y = self.parent.get(x, x)
        if x != y:
            y = self.parent[x] = self.find(y)
        return y

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.find(x) for x in range(n)))