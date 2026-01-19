# a number can only have one divisor, besides 1 and itself, 
# if and if n is the square of a prime number (4, 9, 25, 49, 111, ...).
class Solution:
    def isThree(self, n: int) -> bool:
        # 1 <= n <= 10**4
        hashset = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101 }
        return int(sqrt(n)) * int(sqrt(n)) == n and sqrt(n) in hashset

        