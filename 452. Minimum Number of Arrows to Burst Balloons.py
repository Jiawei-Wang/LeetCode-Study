class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        # sort ballons by their right side
        points.sort(key = lambda x: x[1])

        # greedy
        # each time shot the far right side of current ballon 
        # and check how many ballons are popped 
        arrow = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if arrow >= points[i][0]:
                continue
            
            count += 1
            arrow = points[i][1]

        return count