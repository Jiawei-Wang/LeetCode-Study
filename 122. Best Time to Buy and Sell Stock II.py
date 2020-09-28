# Greedy
# 这个解法最终答案肯定符合要求(所有上升subarray的总和), 但是思考的过程不符合(同时进行买和卖)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans


# 可以多次买卖, 但是多一个限制条件: 不可以同一时间买进卖出, 所以必须提前判断操作时间
# the buying day will be the last continuous day that the price is smallest
# the selling day will be the last continuous day that the price is biggest
# 在连续下降时触底购买, 在连续上升时顶峰卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        n = len(prices)-1
        i = 0
        
        while i < n:
            # 一直往后找, 直到找到低谷, 然后定为买入
            while i < n and prices[i+1] <= prices[i]:
                i += 1
            buy = prices[i]
            # 一直往后找, 直到找到顶峰, 然后定为卖出
            while i < n and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]
            # 然后将该subarray的获利加入profit中
            profit += sell - buy
            
        return profit
    """
    这段代码对于最后一个元素的处理:
    1. 如果它大于前面一个元素, 那么最后一个subarray就会把它计算在内
    2. 如果它小于前面一个元素, 那么它会同时被赋值给buy和sell, 成为单独一个subarray, profit = 0
    """
