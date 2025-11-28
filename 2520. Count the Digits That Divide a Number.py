class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        count = 0
        for digit in digits:
            if num % digit == 0:
                count += 1
        return count