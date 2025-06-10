# total count of number of factors for non-perfect squares is even
# for perfect squares, it is odd 
# so we just need to find how many numbers from 1 to n are perfect squares
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
        