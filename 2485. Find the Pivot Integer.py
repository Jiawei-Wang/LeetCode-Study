class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        x_sq = (n * n + n) // 2 
        sq_rt = int(math.sqrt(x_sq))
        
        if sq_rt * sq_rt == x_sq:
            return sq_rt
        else:
            return -1

