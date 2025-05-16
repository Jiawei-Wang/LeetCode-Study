# n^2
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 1 

        # for every point
        for i in range(len(points)):
            p1 = points[i]

            # we collect the slop info
            count = collections.defaultdict(int)

            # for every other point, we calculate slope 
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
                count[slope] += 1
                # and see what slope leads to most amount of points on same line
                answer = max(answer, count[slope]+1)
        
        return answer