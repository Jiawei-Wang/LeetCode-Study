class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        res = [0] * n
        double = code + code
        
        if k > 0:
            # sum next k elements
            for i in range(n):
                res[i] = sum(double[i+1 : i+1+k])
        else:
            # sum previous |k| elements
            for i in range(n):
                res[i] = sum(double[n + i + k : n + i])
        
        return res
