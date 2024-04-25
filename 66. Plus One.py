# 暴力解：string转integer再+1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number * 10 + i
        number += 1
        string = str(number)
        return [int(i) for i in string] 


# one line 暴力解
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [d for d in str(int(''.join([str(x) for x in digits]))+1)]


# list manipulation
# 三种情况：1.正常+1，2.进位，3.全部进位并加一位
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # case1：正常 + 1
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        if len(digits) == 1:
            return [1,0]
        
        # 找到从末尾开始的连续为9的substring：
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            i -= 1
            
        if i == -1:
            return [1] + [0] * len(digits)
        elif i != len(digits) -1:
            digits[i] += 1
            for x in range(i+1, len(digits)):
                digits[x] = 0
        return digits


# 2024
"""
[1, 2, 4]: modify last element
[1, 2, 9]: modify last two elements
[9, 9]: modify every element and add one digit
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            digit = digits[index]
            if digit == 9: # [1,2,9] will enter here in first loop, enter else in next loop and return
                digits[index] = 0
            else: # [1,2,4] will enter here directly and return
                digits[index] += 1
                return digits
        return [1] + digits # [9,9] will enter if twice, and return here