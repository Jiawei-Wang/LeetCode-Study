"""
instead of tracking index combination
we track maximum profit we have at the end of each choice
1. buy1: max profit after buying 1st stock (will e negative)
2. sell1: max profit after selling 1st stock
3. buy2
4. sell2

state transition:
loop through each day, state is updated based on whether we hold from previous day or transition into new position today
1. buy1: max of keeping previous buy1 or buying today at current price
2. sell1: max of keeping previous sell1 or sell today 
3. buy2: max of keeping previous buy2 or buying today at current price
4. sell2: max of keeping previous sell2 or sell today
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # Initialize states
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        
        for price in prices:
            # 1. Best profit if we bought the 1st stock up to today
            buy1 = max(buy1, -price)
            
            # 2. Best profit if we sold the 1st stock up to today
            sell1 = max(sell1, buy1 + price)
            
            # 3. Best profit if we bought the 2nd stock up to today
            buy2 = max(buy2, sell1 - price)
            
            # 4. Best profit if we sold the 2nd stock up to today
            sell2 = max(sell2, buy2 + price)
            
        return sell2