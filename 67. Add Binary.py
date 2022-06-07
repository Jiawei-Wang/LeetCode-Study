class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if la > lb:
            b = '0' * (la-lb) + b
        elif la < lb:
            a = '0' * (lb-la) + a
            
        ans = ''
        carry = 0
        for i in range(max(la,lb)-1,-1,-1):
            ia = int(a[i])
            ib = int(b[i])
            
            total = ia + ib + carry
            ans += str(total % 2)
            carry = total // 2
        if carry:
            ans += '1'
        
        return ans[::-1]


# 相同算法，代码优化
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]