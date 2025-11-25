class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            digits = [char for char in str(num)]
            digits.sort()
            index = 0
            while digits[index] == "0":
                index += 1
            digits[0], digits[index] = digits[index], digits[0]
            return int("".join(digits))
        elif num == 0:
            return 0
        else:
            num = -num
            digits = [char for char in str(num)]
            digits.sort(reverse = True)
            return -1 * int("".join(digits))
