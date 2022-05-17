from heapq import *

# two heaps for two halves
# logn insert 1 find
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num)) # 将新num放入small中，再将small中最大元素pop出来放入large中，这样避免了large中可能出现元素比small小的case
        else:
            heappush(self.small, -heappushpop(self.large, num)) # 同理

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0]) # large的长度有两种可能：和small相同，或者比small长1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()