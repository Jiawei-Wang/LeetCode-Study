class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n # every number is a Prime initially
        count = 0
        for i in range(2, n):
            if prime[i]: # 2 is a prime
                count += 1 
                j = 2 
                while i*j < n:
                    prime[i*j] = False # everything that is multiply of 2 is marked as False
                    j += 1
        return count
