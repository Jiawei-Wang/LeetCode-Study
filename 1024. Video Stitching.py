"""
1 <= clips.length <= 100
0 <= start[i] <= end[i] <= 100
1 <= time <= 100
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # For each start time, record the furthest end time we can reach
        maxReach = [0] * (T + 1)
        for start, end in clips:
            if start <= T:
                maxReach[start] = max(maxReach[start], min(end, T))
        
        res = 0       # number of clips used
        currEnd = 0   # current coverage
        nextEnd = 0   # furthest reachable with available clips
        
        for i in range(T):
            nextEnd = max(nextEnd, maxReach[i])
            if i == currEnd:  # we need to "switch" clips
                if i == nextEnd:  # cannot extend further
                    return -1
                res += 1
                currEnd = nextEnd
        
        return res
