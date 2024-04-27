# return the size of the smallest interval that contains the query value
# for example intervals = [[1,4],[2,4],[3,6],[4,4]], query = 2, return 3 (size of [2,4])
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {} # key: query, value: answer for this query
        i = 0
        for q in sorted(queries): # sort queries here, cause we still need the original variable for return value
            # first we add intervals that start not later than q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r)) # (interval size, interval end)
                i += 1
            # now heap is sorted by interval size

            # then we pop those that end before q
            """
            this is not absolutely true, if there are only two intervals starting not later than q:
            a long one that ends before q, and a short one that ends not eariler than q
            nothing will be popped and short one will be returned 
            these two will stay in heap and be used for next q
            (so we don't have to pop all that don't satisfy in current loop)
            """
            while minHeap and minHeap[0][1] < q: 
                heapq.heappop(minHeap)

            # because heap is sorted by interval size 
            # the first interval that satisfies (start not later than q) and (end later than q) is the shortest
            res[q] = minHeap[0][0] if minHeap else -1

        # because query is sorted:
        # 1. res needs to be dictionary, because it will be out of order if we use list instead of dictionary
        # 2. next q will be not smaller than current q
        #       1) so the intervals popped don't need to be added back again
        #       2) the remaining ones stay (we don't know if they satisfy new q)
        #       3) we keep adding new ones from intervals list so current index i is brought into next loop
        return [res[q] for q in queries]