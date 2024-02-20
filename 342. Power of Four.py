class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 4:
            if n == 1 or n == 4:
                return True
            return False
        
        power = 1
        current = 4 ** power
        while current < n:
            power += 1
            current *= 4
            if current == n:
                return True
        return False