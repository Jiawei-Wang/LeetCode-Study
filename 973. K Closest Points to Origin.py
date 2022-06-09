# time 1200 ms
# space 20 mb
import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for i in points:
            h.heappush(l, (i[0]*i[0]+i[1]*i[1], i))
        
        return [x[1] for x in h.nsmallest(k, l)]


# 和上面的解time space都差不多
# 区别是只保留k个元素
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:        
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]