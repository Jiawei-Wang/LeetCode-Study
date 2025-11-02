class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent_of = defaultdict(list)
        for x, y in edges:
            parent_of[x].append(y)

        ans = [[] for _ in range(n)]

        def dfs(x, curr):
            for parent in parent_of[curr]:
                if ans[parent] and ans[parent][-1] == x: 
                    continue
                ans[parent].append(x)
                dfs(x, parent) 

        for i in range(n): 
            dfs(i, i)
        return ans