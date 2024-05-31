"""
s0: no stock, we either didn't have stock yesterday, or sold stock yesterday
s1: have stock, we either had stock yesterday, or bought stock yesterday
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        s0 = [0] * length
        s1 = [0] * length

        s1[0] = -prices[0]

        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])

        return s0[-1]
        