# 直接让myPow使用built in function
# 解释： https://stackoverflow.com/questions/30693639/why-does-class-x-mypow-pow-work-what-about-self
class Solution:
    myPow = math.pow


# 依旧使用built in
class Solution:
    def myPow(self, x, n):
        return x ** n


# Time Limit Exceeded
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x and n are not both 0
        if x == 0:
            return 0
        if n == 0:
            return 1

        ans = x
        for i in range(abs(n)-1):
            ans *= x
        
        return ans if n > 0 else 1/ans


# recursion
"""
理解：
1. 一共分为3个case，n = 0，n为正整数，n为负整数
2. n=0直接给出答案，同时其又作为正整数case的base case
2. 负整数case可以直接转变为正整数来计算
3. 正整数的case可以通过recursion最终走到n=0的case
4. 节约计算时间，如果n是2的倍数，则可以直接通过让x = x^2的方式来让n减去一半
"""
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        
        # if n is positive integer and is multiple of 2: 
        return self.myPow(x*x, n/2)


# iteration
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # a^b = (1/a)^-b
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n:
            if n & 1: # if n % 2
                ans *= x
            x *= x
            n >>= 1 # n // 2 
        return ans