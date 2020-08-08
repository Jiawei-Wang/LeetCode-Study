# iteration
class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        first = 0
        second = 1
        for i in range(2, N+1):
            ans = first + second
            first = second
            second = ans
        return ans

# recursion
class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0;
        if N == 1: return 1;
        return self.fib(N-1) + self.fib(N-2)


# Aug 8 2020
# pure recursion
class Solution:
    def fib(self, N: int) -> int:
        if N ==0: return 0
        if N == 1: return 1
        return self.fib(N-1)+self.fib(N-2)


# Iteration
class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        first = 0
        second = 1
        i = 2
        while i <= N:
            first, second = second, first+second
            i+=1
        return second
