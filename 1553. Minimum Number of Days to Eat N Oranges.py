# simple dp
# time limit exceeded
class Solution:
    def minDays(self, n: int) -> int:
        dp = [float('inf')] * (n+1) # dp[i] = k: at least k days to finish i oranges
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            one = dp[i-1] + 1
            if not i % 2:
                two = dp[i//2] + 1  
            else:
                two = float('inf')
            if not i % 3:
                three = dp[i//3] + 1
            else:
                three = float('inf')
            dp[i] = min(one, two, three)
        return dp[-1]


# optimal solution:
#   1. if can be divided by 3, do it
#   2. if not:
#       1- if it's even number, divided by 2
#       2- if it's odd number, -1 then divided by 2
class Solution:
    @cache
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))

# TODO: math proof for this solution to be optimal