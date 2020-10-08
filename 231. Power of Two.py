# 解法1：步进
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False

        power = 0
        while 2 ** power < n:
            power += 1
        if 2 ** power == n:
            return True
        else:
            return False
