class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 最后要pop末尾的0，所以先处理一下corner case，避免指针越界
        if num1 == '0' or num2 == '0':
            return '0'
         
        # 先把两个string转换成int list
        n1 = [int(char) for char in num1][::-1] # 例：num1 = '123', n1 = [3,2,1]
        n2 = [int(char) for char in num2][::-1]
        l1 = len(num1)
        l2 = len(num2)
        
        # 两个数相乘最大可能值长度是两者之和，例：999*99 = 98901
        ans = [0] * (l1+l2)
        
        # 先相乘，获得n1的每一位数和n2所有位数的乘积
        # 再相加，将每个乘积放入对应位置并进位
        for i in range(l1):
            carry = 0
            # n1的第i位和n2所有数字相乘的结果是从第i位一直到第(i+l2-1)位，并有可能进位至（i+l2)
            for j in range(l2):
                # 两点要考虑
                # 1.本轮上一个位置的乘积可能带有进位信息
                # 2.之前几轮的for loop的乘积结果可能已经对ans[i+j]有了写入
                ans[i+j] += n1[i] * n2[j] + carry 
                carry = ans[i+j] // 10
                ans[i+j] %= 10
            ans[i+j+1] += carry

        # 然后解决可能存在的尾部为0的corner case并翻转list
        while ans[-1] == 0:
            ans.pop()
        return ''.join([str(x) for x in ans][::-1])


# 2024
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # corner case
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2)) # the maximum length of the product of two integers is len(num1) + len(num2): 99*99=9801
        num1, num2 = num1[::-1], num2[::-1] # go from back to front
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2]) # 0 <= product <= 81
                # for example: 123 * 456:
                # 3*6 starts on 1's digit
                # 2*6 starts on 10's digit
                # 3*5 starts on 10's digit
                # 2*5 starts on 100's digit
                res[i1 + i2] += product # res[i1+i2] already contains all the previous carries
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, begin = res[::-1], 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        res = map(str, res[begin:]) # a map object containing strings
        return "".join(res)
