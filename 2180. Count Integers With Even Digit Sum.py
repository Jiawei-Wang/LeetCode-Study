# simulation
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            # Calculate digit sum
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum % 2 == 0:
                count += 1
        return count


"""
in any consecutive block of 10 numbers (for example 0-9 or 10-19)
there are 5 even digit sum numbers, 5 odd digit sum numbers
so for an number num:
we have num//10 blocks, each has 5 

if num itself has even digit sum, then from 1 to num we have num//2 in total
if num itself has odd digit sum, then from 1 to num we have (num-1)//2 in total

overall: (num- (digit_)
"""
class Solution:
    def countEven(self, num: int) -> int:
        # Calculate the digit sum of num
        digit_sum = sum(int(d) for d in str(num))

        # Apply the math trick
        return (num - (digit_sum % 2)) // 2