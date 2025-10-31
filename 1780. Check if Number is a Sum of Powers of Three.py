class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # turn number into base-3
        # each digit can only be 1 or 0, but not 2
        # for example 
        # 91 = 1 * 3^4 + 0 * 3^3 + 1 * 3^2 + 0 * 3^1 + 1 * 3^0
        # 46 = 1 * 3^3 + 2 * 2^2 + 0 * 3^1 + 1 * 3^0
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        
        return True