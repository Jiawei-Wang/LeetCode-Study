class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)

        # Build union-find structure
        for a, b in pairs:
            dsu.union(a, b)

        # Group indices by root
        components = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)

        # Build result as a list of characters
        res = list(s)

        # For each component, sort letters and place them back
        for indices in components.values():
            chars = sorted(res[i] for i in indices)     # extract and sort chars
            for idx, ch in zip(sorted(indices), chars): # put back sorted chars
                res[idx] = ch

        return "".join(res)




        