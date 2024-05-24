class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        # first integer in ascending order
        # second integer in descending order
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        count = 1
        current = 0 # index = 0
        for i in range(1, len(intervals)):
            if intervals[current][1] >= intervals[i][1]:
                continue
            else:
                count += 1
                current = i
        
        return count


