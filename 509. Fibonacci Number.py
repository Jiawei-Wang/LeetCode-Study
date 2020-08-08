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


# Recursion + Memoization (Top Down)
# initialize a lookup array
# search the result before computing
# if no result, compute and store result
class Solution:
    def fib(self, N: int) -> int:
        ans = [0] * 31
        if N <= 1:
            ans[N] = N
            return ans[N]
        if ans[N] != 0:
            return ans[N]
        else:
            ans[N] = self.fib(N-1)+self.fib(N-2)
        return ans[N]


# Bottom up
class Solution:
    def fib(self, N: int) -> int:
        ans = [0] * 31
        ans[1] = 1

        i = 2
        while i <= N:
            ans[i] = ans[i-1] + ans[i-2]
            i += 1
        return ans[N]
