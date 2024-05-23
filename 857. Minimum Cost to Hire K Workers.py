# pick k elements from a list of n elements
# for each element: 
#     ratio = wage / quality
#     wage = max(wage, quality * max(ratio of all picked elements))
# return minimum sum(wage) 
# thoughts:
# 1. we can sort the input from lowest ratio to highest ratio
# 2. then we sort the input from lowest quality to highest quality
# 3. we then pick each element and see if target can be lowered
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        combined = sorted(zip(quality, wage), key=lambda x: (x[1] / x[0], x[0]), reverse=False)
        # for example
        # quality =  [10, 20, 5,  10]
        # wage =     [70, 50, 30, 25]
        # combined = [(10, 25), (20, 50), (5, 30), (10, 70)]
        # lower ratio first, for same ratio, lower quality first

        pq = []
        quality_sum = 0
        target = float('inf')

        for q, w in combined:
            heapq.heappush(pq, (-q))
            quality_sum += q
            
            if len(pq) > k:
                quality_sum += heapq.heappop(pq)
                ratio = w/q 
                target = min(target, quality_sum * ratio)
            elif len(pq) == k:
                ratio = w/q 
                target = min(target, quality_sum * ratio)

        return target 