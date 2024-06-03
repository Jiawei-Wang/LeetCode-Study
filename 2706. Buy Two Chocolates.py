class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = float('inf')
        second = float('inf')
        for price in prices:
            if price < first:
                second = first
                first = price
            elif price < second:
                second = price
        
        left = money - first - second
        return left if left >= 0 else money


        