class Solution:
    def findNthDigit(self, n: int) -> int:
        number = 1
        digit = 0
        while digit < n:
            string = str(number)
            length = len(string)
            if digit + length >= n:
                return int(string[n - digit - 1])
            number += 1
            digit += length


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        # single digit number (1 to 9) in total has 9*1=9 digits
        # double digit number (10 to 99) in total has (99-9)*2=180 digits
        # triple digit number (100 to 999) in total has (999-99)*3=2700 digits
        # n digit number (10^(n-1) to 10^n-1) in total has ((10^n-1) - (10^(n-1)-1))*n = 9n*10^(n-1) digits
        """
        if n <= 9:
            return n
        currentDigit = 1
        currentTotal = 9
        while currentTotal < n:
            currentDigit += 1
            newAdd = 9 * currentDigit * (10 ** (currentDigit-1))
            if currentTotal + newAdd >= n:
                diff = n - currentTotal
                count = diff // currentDigit 
                mod = diff % currentDigit
                if mod == 0:
                    targetNumber = 10 ** (currentDigit - 1) + count - 1
                    return int(str(targetNumber)[-1])
                else:
                    targetNumber = 10 ** (currentDigit - 1) + count
                    return int(str(targetNumber)[mod-1])
            currentTotal += newAdd


        