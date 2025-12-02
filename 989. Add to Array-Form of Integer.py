class Solution:
    def addToArrayForm(self, num1: List[int], k: int) -> List[int]:
        num1 = num1[::-1]
        num2 = [int(x) for x in str(k)][::-1]
        length1 = len(num1)
        length2 = len(num2)

        if length1 <= length2:
            num1, num2 = num2, num1
            length1, length2 = length2, length1
        
        carry = 0
        for index in range(length2):
            total = num1[index] + num2[index] + carry
            digit = total % 10
            carry = total >= 10
            num1[index] = digit
        
        for index in range(length2, length1):
            total = num1[index] + carry
            digit = total % 10
            carry = total >= 10
            num1[index] = digit
        
        if carry:
            num1.append(1)
        
        return num1[::-1]

