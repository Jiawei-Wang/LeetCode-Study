class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(current):
            if len(current) == k:
                answer.append(current)
            
            cur_num = current[-1]
            for num in range(cur_num + 1, n+1):
                dfs(current + [num])
            
        
        for start in range(1, n+1):
            dfs([start])
        
        return answer