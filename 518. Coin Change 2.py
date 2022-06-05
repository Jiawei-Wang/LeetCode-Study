# 至少有一个coin
# coins的数额永远为正数
# amount不为负
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for j in coins:
            for i in range(0, amount+1):
                if i + j < amount+1:
                    dp[i+j] += dp[i]
        
        return dp[-1]
    
        # 错误答案：
        # for i in range(1, amount+1):
        #     for j in coins:
        #         if i - j >= 0:
        #             dp[i] += dp[i-j]
        
        
"""
对于为什么第一个for循环必须是coins的理解：
假设coins = [2,5]，target = 7
因为先使用2，再使用5，来组成一个7
和先使用5，再使用2，来组成一个7
是同一个组合，所以如果使用错误答案中的for循环
我们就会让dp[7] = dp[2] + dp[5]

而使用正确答案中的循环顺序，可以保证每个coin是被按顺序添加
即我先只使用2来找到所有可能的总和，再加入5
不会出现先2后5，和先5后2同时出现的场景
"""