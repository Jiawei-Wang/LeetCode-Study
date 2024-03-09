class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Assume dp[i] is the fewest number of coins making up amount i
        # then for every coin in coins, dp[i] = min(dp[i - coin] + 1)
        dp = [0] + [float('inf') for i in range(amount)] # 初始化需要 inf 个硬币
        for i in range(1, amount+1): 
            for coin in coins:
                if i - coin >= 0: # 这里的意思是检测index是否出界
                    dp[i] = min(dp[i], dp[i-coin] + 1) # 第i位置上所需硬币数量 = 第i-coin位置上所需硬币数量 + 1
        if dp[-1] == float('inf'): # 如果没有任何一个dp[i-coin]可以走到dp[i]，dp[i]在遍历结束时即为 inf
            return -1
        return dp[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # no coin is worth 0 so we need a starting point
        # this covers the corner case: if amount is 0 we will return 0
        dp = [0] + [float('inf')] * amount 

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1