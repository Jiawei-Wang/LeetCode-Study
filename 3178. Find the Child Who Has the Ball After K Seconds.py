class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        rounds = k // n
        remain = k % n 

        if rounds % 2 == 0:
            return remain
        else:
            return n - remain