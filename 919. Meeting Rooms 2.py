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
