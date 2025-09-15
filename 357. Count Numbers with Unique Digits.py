class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # dp
        # let f(n) = count of numbers of length n with unique digits 
        # f(1) = 10: every number is unique
        # f(2) = 9 * 9: first digit is from 1 to 9, second digit is from 0 to 9 different from first
        # f(3) = f(2) * 8: third digit is from 0 to 9 different from both first and second
        # f(4) = f(3) * 7
        # ........
        # f(10) = f(9) * 1
        # any number longer than 10 digits with unique digits doesn't exist
        if n == 0: return 1
        answer = 10
        unique_digits = 9
        available_numbers = 9
        while n > 1 and available_numbers > 0:
            unique_digits *= available_numbers
            answer += unique_digits
            available_numbers -= 1
            n -= 1
        return answer
