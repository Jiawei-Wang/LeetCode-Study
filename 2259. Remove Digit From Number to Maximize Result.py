class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # 从左侧开始检查，若目标digit后方数字更大则移除此digit，否则移除最后一个digit
        for i in range(len(number)-1):
            if number[i] == digit and number[i+1] > digit:
                return number[:i] + number[i+1:]
            last = number.rfind(digit) # string.rfind(str): 从右侧开始找到string中的第一个str
        return number[:last] + number[last+1:]