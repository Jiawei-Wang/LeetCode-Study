# dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for nei, adj in enumerate(isConnected[node]): 
                # isConnected[node] = a list of whether or not i-th city is connected with node-th city
                # 举例：isConnected[0] = [1,0,1], 表示第0个城市和第0个城市相连，第1个和第0个不相连，第2个和第0个相连
                # nei: 0, 1, 2
                # adj: 1, 0, 1
                if adj and nei not in seen: # 如果两者相连（adj=1）且nei-th城市还未被遍历过
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        seen = set()
        for i in range(len(isConnected)): # 虽然是2d list但是只有len(list)个元素
            if i not in seen: 
                dfs(i)
                ans += 1
        return ans


# 下面这个答案没看明白，还要再研究
# union find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        n = len(M)
        uf = {i:i for i in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1:
                    uf[find(i)] = find(j)
        
        return sum([1 for k, v in uf.items() if k == v])