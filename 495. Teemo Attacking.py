class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        end = 0
        for time in timeSeries:
            if time >= end:
                count += duration
            else:
                count += time + duration - end
            end = time + duration
        return count