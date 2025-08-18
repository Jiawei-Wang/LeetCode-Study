import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smol = float('inf')
        big = -float('inf')
        for num in nums:
            if num < smol:
                smol = num
            if num > big:
                big = num
        return math.gcd(big, smol)