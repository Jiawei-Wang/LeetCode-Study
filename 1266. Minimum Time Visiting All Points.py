class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        # 拿到题的第一想法：其实就是求Chebyshev distance
        # 找到各坐标数值差最大的那个即可
        total_dis = 0
        for i in range(1,len(points)):
            total_dis += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
        return total_dis
