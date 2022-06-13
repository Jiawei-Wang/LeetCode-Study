class Solution:
    """
    python2解法：
        s = cmp(x, 0)               cmp() returns -1/0/1
        r = int(`s*x`[::-1])        这句话意思是把 s 的所有数字倒过来，同时忽略 s 本身的正负
        return s*r * (r < 2**31)    乘 True 得到原数字，乘 False 得到 0
    """
    # python3解法：
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)


# 将一个整数翻转过来，正常情况下每次剥离现有数字的最后一位数，然后赋给新的数字即可
# 这道题考察的是overflow，32位整数的范围为：[-2^31, 2^31 - 1]，所以翻转得到的数字可能会超过此边界而overflow
# 所以我们需要保证任何时候newResult都没有overflow
class Solution:
    def reverse(self, x: int) -> int:
        digit = 1
        if x < 0:
            digit = -1
            x = abs(x)
        result = 0
        while x:
            tail = x % 10
            newResult = result * 10 + tail
            if (newResult - tail)//10 != result: # 发生越界导致newResult错误
                return 0
            result = newResult
            x //= 10
        return digit * result
    
"""
上面的答案在python3上无效，因为虽然newResult大于2^31-1但是python3判断未越界，需要手动提供边界数字
"""


class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10)) # 防止出现 -1 % 10 = 9
            x = int(x/10)                 # 防止出现 -1 //10 = -1
            
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)) or \
            (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = res * 10 + digit
        return res