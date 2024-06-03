class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n != 1:
            count += n//2
            if n % 2:
                n = n//2 + 1
            else:
                n //= 2

        return count 