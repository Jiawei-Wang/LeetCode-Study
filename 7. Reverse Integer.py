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
