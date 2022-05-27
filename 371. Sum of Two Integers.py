# TODO: 不理解，还要重新看

class Solution:
    def getSum(self, a: int, b: int) -> int:
#         此答案无法处理负数        
#         carry = 0
#         while b:
#             carry = a & b # 如果为1，说明a，b此位上都是1，那么进位
#             a = a ^ b # a ^ b 是不会进位的 a + b
#             b = carry << 1
#         return a
        
        def add(a, b): 
            if not a or not b:
                return a or b
            return add(a^b, (a&b) << 1)

        if a*b < 0: # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b: # -a == b
                return 0
            if add(~a, 1) < b: # -a < b
                return add(~add(add(~a, 1), add(~b, 1)),1) # -add(-a, -b)

        return add(a, b) # a*b >= 0 or (-a) > b > 0 