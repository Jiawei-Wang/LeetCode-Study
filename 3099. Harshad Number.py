class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum([int(digit) for digit in str(x)])

        if x % digit_sum:
            return -1
        
        return digit_sum