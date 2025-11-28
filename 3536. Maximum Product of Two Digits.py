class Solution:
    def maxProduct(self, n: int) -> int:
        array = [int(digit) for digit in str(n)]
        biggest = -1
        second = -1
        for digit in array:
            if digit >= biggest:
                biggest, second = digit, biggest
            elif digit > second:
                second = digit
        
        return biggest * second