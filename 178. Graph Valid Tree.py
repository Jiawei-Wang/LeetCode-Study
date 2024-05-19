"""
input:
1. n nodes labeled from 0 to n-1
2. a list of undirected edges
output:
check whether these edges make up a valid tree

an undirected graph is a tree if:
1. all vertices are connected
2. no circle
"""

# dfs on graph
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n:
            return True
        
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)


# union-find style
class Solution:
    def __find(self, n: int) -> int:
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        self.parents = {}
        self.heights = {}
        self.components = n

        for n1, n2 in edges:
            if self.__find(n1) == self.__find(n2):  # 'redundant' edge
                return False
            self.__connect(n1, n2)

        return self.components == 1  # forest contains one tree