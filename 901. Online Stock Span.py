class StockSpanner:

    def __init__(self):
        self.stack = deque()
        
    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        else:
            count = 1
            while self.stack and self.stack[-1][0] <= price:
                prev = self.stack.pop()
                count += prev[1]
            self.stack.append((price, count))
            return count


    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)