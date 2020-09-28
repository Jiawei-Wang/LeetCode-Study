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