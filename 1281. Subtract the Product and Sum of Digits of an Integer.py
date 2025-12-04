class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        array = [int(char) for char in str(n)]

        product = 1
        total = 0

        for digit in array:
            product *= digit
            total += digit
        
        return product - total
