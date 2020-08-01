class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange > numBottles:
            return numBottles
        ans = numBottles
        left = numBottles
        while left >= numExchange:
            ans += left // numExchange
            left = left // numExchange + left % numExchange
        return ans
