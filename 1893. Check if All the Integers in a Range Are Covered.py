# line sweep
# general idea: for each interval start, count += 1, for each interval end, count -= 1
# then we go through whole input range to calculate count at given time
# here 1 <= start, end, left, right <= 20 so the input range is small
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        line = [0] * 52 # time is inclusive so for [1, 50] we prepare [0, 51]
        for r in ranges:
            line[r[0]] += 1
            line[r[1]+1] -= 1
        
        overlaps = 0
        for i in range(1, right+1): # we start from 1 rather than left since we need the count
            overlaps += line[i]
            if i >= left and overlaps == 0: # if there is a time between left and right, and we don't have any overlap left
                return False
        
        return True