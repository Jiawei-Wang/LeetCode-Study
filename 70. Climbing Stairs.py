class Solution:
    def climbStairs(self, n: int) -> int:
        # 到达第n个台阶的方法 = 到达第n-1个台阶的方法 + 到达第n-2个台阶的方法
        
        if n == 1: return 1
        if n == 2: return 2
        
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]


# 学习不同的dp/recursion写法



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        first = 1
        second = 2
        current = 2
        while current < n:
            current += 1
            first, second = second, first + second
            
        return second