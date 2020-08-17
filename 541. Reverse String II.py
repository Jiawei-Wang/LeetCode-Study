# 解法1：转换成char array
class Solution(object):
    def reverseStr(self, s, k):
        # 直接转换成array
        a = list(s)
        # 设定步进距离
        for i in range(0, len(a), 2*k):
            # 直接翻转
            a[i:i+k] = reversed(a[i:i+k])
        # 将array转换回sting
        return "".join(a)
        
