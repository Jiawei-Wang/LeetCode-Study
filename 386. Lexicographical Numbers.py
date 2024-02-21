class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur, n, res):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                if 10*cur+i>n:
                    return 
                dfs(10*cur+i, n, res)
        res = []
        for i in range(1, 10):
            dfs(i, n, res)
        return res
            