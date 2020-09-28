# DP
class Solution:
    def numDecodings(self, s: str) -> int:
        # 两个会让结果变成0的corner case
        if not s or s[0]=='0':
            return 0
        
        # 对于所有非上方corner case的string, 答案肯定至少为1
        #  设置第一个元素做缓冲, 可以避免很多corner case的判断
        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization (第一个1是缓冲, 第二个1代表s[0]的可能组合有1个)
        dp[0:2] = [1,1]

        # 从下标为2开始(指向的是s的第二个字符(下标为1))
        for i in range(2, len(s) + 1): 
            # 对于这个元素, 它有两种情况, 
            # 1. 作为单独的元素存在(继承dp[i-1]的值), 
            # 2. 和前面一个形成二连(继承dp[i-2]的值)
            
            # 只要该位置数字大于0, 则dp[i]自动获得和dp[i-1]相同的值
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i - 1]
            # 如果再额外符合10~26之间的要求, 可以再获得dp[i-2]的值
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[-1]
    
"""
这个解法的重点是解决了很多corner case
1. 长度为0
2. 以0开始
3. 以0结尾
4. 中间有多个连续的0
5. etc
而我自己的解法: 分为多个substring, 然后把每个substring的所有组合数相乘, 出现的问题是过多的corner case
比如: 11299112 可以变成 3*3=9
但是: 011, 110, 11001等都需要额外的判断语句, 过于繁琐
"""