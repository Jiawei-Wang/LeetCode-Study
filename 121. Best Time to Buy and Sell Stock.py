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


# 解法2: one pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > high:
                high = prices[i] - low
        
        return high

    """
    对于这个解法的理解:
    low这个变量通过遍历, 会最终指向array中最小的那个元素
    所以遍历结束时它指向的那个元素不一定是输出的答案所对应的那个元素 
    而high暂存的是: 上一个low后面找到的最大差值, 所以low在每次找到更小的元素时就可以直接更新
    """

# 05-09-2022
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 暴力解
        # ans = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         ans = max(ans, prices[j]-prices[i])
        # return ans
        
        # two pointer       
        l, r = 0, 1 # l: buy, r: sell
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp: 和53 maximum subarray逻辑相同，如果之前几天总和为负，那么就将新的最佳买入日期设定为今天
        maxCur = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0, maxCur) 

            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar