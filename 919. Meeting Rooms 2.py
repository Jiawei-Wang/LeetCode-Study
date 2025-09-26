# an array of meeting time intervals, return the minimum number of conference rooms needed
# understanding: find the maximum number of overlaps at one time

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # each interval doesn't matter (start doesn't have to match end)
        # we only care about total number of intervals at one time
        # so we only keep track of number of starts and ends
        # for example: [[0, 30], [5, 10], [15,25]]
        # 1 room needed at 0
        # 2 rooms needed at 5
        # 1 room needed at 10 (a meeting ended)
        # 2 rooms needed at 15
        # 1 room needed at 25
        
        time = []
        for start, end in intervals:
            time.append((start, 1)) # 1 means a meeting is added
            time.append((end, -1)) # -1 means a meeting is ended
        
        time.sort(key=lambda x: (x[0], x[1]))
        # time = [[0,1], [5,1], [10,-1], [15,1], [25,-1], [30,-1]]
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count


# 2025
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
min heap
nlogn time, n space
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) 
        # if two have same start different end
        # the sorting algorithm treats them as same object
        # so they won't be touched
        # but it's ok since we don't need end to be sorted

        min_heap = []

        for interval in intervals: 
        # we start from early start meetings
            if min_heap and min_heap[0] <= interval.start:
            # if earliest end meeting has ended, we free the room for new meeting
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            # regardless which room new meeting takes, it is added to the heap

        return len(min_heap) 
        # why len(min_heap) at the end rather than max len(min_heap) at any time:
        # each iteration, len(min_heap) will either += 1 (a new meeting room for the new meeting)
        # or stay the same (the earilest end meeting has ended and freed a room for the new meeting)
        # so len(min_heap) at the end is the biggest at any time

        
# sweep line
# usually it's using a counter and iterate through all possible time points
# but since time range is huge, we need to hashmap to store 
# time points that are in the input
# still nlogn time and n space since we need to keep hashmap and sort hashmap
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hashmap = defaultdict(int)
        for i in intervals:
            hashmap[i.start] += 1
            hashmap[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(hashmap.keys()):
            prev += hashmap[i]
            res = max(res, prev)
        return res


# two pointers
# same logic as sweep line
# also needs sorting so nlogn time
# and also n space for keeping the input data
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


# greedy: also same idea as sweep line
# nlogn time: sort
# n space: keep input data
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res