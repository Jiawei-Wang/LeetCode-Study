# union find + string match
class Solution:
    def numSimilarGroups(self, a):
        n = len(a)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                # given constraint: all words in input have the same length and are anagrams of each other.
                if sum(a[i][k] != a[j][k] for k in range(len(a[i]))) in (0, 2):
                    uf.union(i, j)

        return len(set(uf.find(i) for i in range(n)))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    # without path compression
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    # with path compression
    # def find(self, x):
    #   if x != self.parent[x]:
    #     self.parent[x] = self.find(self.parent[x])
    #   return self.parent[x]


    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


# improved version
class Solution:
    def numSimilarGroups(self, strs):
        n = len(strs)
        uf = UnionFind(n)

        def similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2: # early break
                        return False
            return diff == 0 or diff == 2

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    uf.union(i, j)

        return uf.count


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n # extra variable to keep track of groups

    # path compression
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        self.count -= 1
