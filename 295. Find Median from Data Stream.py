# two heaps for two halves
# (logn) insert (1) find
from heapq import * # this syntax allows us to not write "heapq.heappush" anymore
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    # we let large half equal to or longer than small half by 1
    def addNum(self, num):
        if len(self.small) == len(self.large): # so now we want to insert into large
            # but we don't know if current element belongs to small or large
            # so we insert it into small, and take the biggest one from small and insert into large
            heappush(self.large, -heappushpop(self.small, -num))  
        else: # same logic, we insert into large and take the smallest from large and insert into small
            heappush(self.small, -heappushpop(self.large, num)) 

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else: # large has one more element than small
            return float(self.large[0]) 
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        self.first = [] # max heap for smaller elements
        self.second = [] # min heap for bigger elements

    def addNum(self, num: int) -> None:
        # we keep first equal to second or longer than second by 1
        if not self.first: # if both are empty, pick first
            heapq.heappush(self.first, -num)
        else:
            if len(self.first) == len(self.second) + 1: # pick second
                current = -heapq.heappop(self.first)
                smaller, bigger = min(num, current), max(num, current)
                heapq.heappush(self.first, -smaller)
                heapq.heappush(self.second, bigger)
            else: # pick first
                current = heapq.heappop(self.second)
                smaller, bigger = min(num, current), max(num, current)
                heapq.heappush(self.first, -smaller)
                heapq.heappush(self.second, bigger)
                

    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        else:
            return (-self.first[0] + self.second[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()