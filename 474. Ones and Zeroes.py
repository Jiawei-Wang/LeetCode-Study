# dfs
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        most = 0

        def count(string):
            zero = 0
            one = 0
            for char in string:
                if char == "0":
                    zero += 1
                else:
                    one += 1
            return (zero, one)

        def dfs(m, n, i, total):
            nonlocal most 

            if m < 0 or n < 0:
                return 
            if i == length and m >= 0 and n >= 0:
                most = max(most, total)
                return
            
            deduction = count(strs[i])
            dfs(m, n, i+1, total)
            dfs(m-deduction[0], n-deduction[1], i+1, total+1)
            return 

        dfs(m, n, 0, 0)
        return most


# dfs + cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        cache = dict()

        def count(string):
            zero = 0
            one = 0
            for char in string:
                if char == "0":
                    zero += 1
                else:
                    one += 1
            return (zero, one)

        def dfs(m, n, i):
            if m < 0 or n < 0:
                return -1
            if i == length:
                return 0
            if (m, n, i) in cache:
                return cache[(m, n, i)]
            
            deduction = count(strs[i])
            exclude = dfs(m, n, i+1)
            include = 1 + dfs(m-deduction[0], n-deduction[1], i+1)
            cache[(m, n, i)] = max(exclude, include)
            return cache[(m,n,i)]

        return dfs(m, n, 0)