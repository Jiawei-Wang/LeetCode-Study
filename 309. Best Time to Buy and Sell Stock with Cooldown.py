"""
思维过程：
1. 穷举：每个元素有三种可能状态：buy/sell/cooldown，所以可以穷举每一种组合，并从符合要求的组合中找出最大值
2. decision tree：与其列举一堆不符合要求的组合，可以从第一个元素开始，给它赋予buy/cooldown的状态，然后后续元素分出不同的状态，这样保证了每个分支都是符合要求的
3. dp：decision tree + memory

对于dp的思考：
state machine: 一共三种状态，s0，s1，s2
    s0：无股票，此时可以选择cooldown（下一个元素依旧s0），或者buy，下一个元素进入s1
    s1：持有股票，此时可以选择cooldown（下一个元素依旧s1），或者sell，下一个元素进入s2
    s2：无股票，此时只有一个选择：cooldown，然后下一个元素进入s0

s0[i] = max(s0[i-1], s2[i-1])               # i处于s0状态可能有两种情况：i-1时在s0或者i-1时在s2
s1[i] = max(s1[i-1], s0[i-1] - prices[i])   # i处于s1状态可能有两种情况：i-1时在s1或者i-1时在s0
s2[i] = s1[i-1] + prices[i]                 # i处于s2状态只有一种情况：i-1时在s1
所以我们要找出s0和s2的最大值

base case：
s0[0] = 0           
s1[0] = -price[0] 
s2[0] = float('-inf')
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n <= 1:
            return 0
        
        s0 = [0] * n
        s1 = [-prices[0]] + [0] * (n - 1)
        s2 = [float('-inf')] + [0] * (n - 1)
        
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])   
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[-1], s2[-1])