# 读题感想: 找出最大差值

# 解法1: 暴力解, 列举所有可能性
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1: return 0
        ans = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans


