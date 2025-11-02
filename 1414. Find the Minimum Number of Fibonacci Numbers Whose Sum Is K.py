class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        res, a, b = 0, 1, 1
        # find the biggest number that is <= k
        while b <= k:
            a, b = b, a + b
        # then find the biggest number that can be deducted from k
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res