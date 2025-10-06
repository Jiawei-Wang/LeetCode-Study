# greedy: no garden has more than 3 neighbors so there will 
# always be at least one color to choose from
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # adj list 
        adj = [[] for i in range(n)]
        for x, y in paths:
            adj[x - 1].append(y - 1)
            adj[y - 1].append(x - 1)

        res = [0] * n
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in adj[i]}).pop()
        return res