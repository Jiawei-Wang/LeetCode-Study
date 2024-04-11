# 2024
"""
2d dp:

1. every row is a coin
2. every column is an amount, last position is the target amount
3. at every position, we can choose any one coin from coins
4. to prevent duplicate: [1,1,2] is the same as [2,1,1] or [1,2,1]:
    we do not allow picking smaller coins: if 2 is picked, following coins cannot be smaller than 2
    so [2,1,1] and [1,2,1] are no more

for example: amount = 5, coins = [1,2,5]
grid looks like 
        5   4   3   2   1   0
    1                       1 <- only one way to sum up to 0
    2                       1 <- how many ways can we sum up to 0 using 2 and 5
    5                       1 <- how many ways can we sum up to 0 using only 5 (if we pick 5 we cannot pick other coins)

computation order: right to left, bottom to top
how to do it:
to get to 1 using only 5s, we need to check -4, since -4 is out of bound, there is 0 way to do it
to get to 1 using 2s and 5s, we need to check -1 and 5s position, there is 0 + 0 way to do it
to get to 1 using 1s, 2s, and 5s, we need to check 0 and 2s position, there is 1 + 0 way to do it

so this answer can actually turn into 1d dp by only keeping two arrays
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # create 2d array
        dp = []
        for i in range(len(coins)):
            dp.append([0]*amount+[1]) # last column is filled out

        # fill out first row 
        last_row = len(coins) - 1
        coin = coins[last_row]
        for column in range(amount-1, -1, -1):
            current = amount - column
            if current % coin == 0:
                dp[last_row][column] = 1
            else:
                dp[last_row][column] = 0

        # rest of rows
        for row in range(len(coins)-2, -1, -1):
            for column in range(amount-1, -1, -1):
                coin = coins[row]
                current = amount - column
                if current - coin < 0:
                    dp[row][column] = dp[row+1][column]
                else:
                    dp[row][column] = dp[row][column + coin] + dp[row+1][column]
                        
        return dp[0][0]


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