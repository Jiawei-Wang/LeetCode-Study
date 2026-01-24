class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(n):
            rn = 0
            while n:
                rn = rn * 10 + n % 10
                n //= 10
            return rn

        for n in range(num // 2, num + 1):
            if n + reverse(n) == num:
                return True

        return False