# to break number N into two factors
# the best factors should be 
# (N/2)*(N/2) when N is even or (N-1)/2 *(N+1)/2 when N is odd
# and we should do the break when the product > N
# if (N/2)*(N/2) > N, then N > 4
# if (N-1)/2 *(N+1)/2 > N, then N >= 5
# so a factor has to be at most 4 
# otherwise it can be broken into two smaller factors
# also for all possible factors:
# 4 = 2*2, so factor 4 is equal to two factor 2s, we don't need to write code for 4
# 3*3 > 2*2*2, therefore the optimal product should contain no more than three factor 2s
# factor 1 is not needed
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product 