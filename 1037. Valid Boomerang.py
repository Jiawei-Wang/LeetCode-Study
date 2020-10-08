class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 取前两个点，判断是否是同一个点，如果不是，获得直线的函数
        y2 = points[1][1]
        y1 = points[0][1]
        x2 = points[1][0]
        x1 = points[0][0]
        y3 = points[2][1]
        x3 = points[2][0]

        if y2 == y1 and x2 == x1:
            return False
        # corner case: 如果两个点垂直，则只需要判断第三个点是否 x 值相等
        elif x2 == x1:
            if x3 == x1: return False
            else:
                return True
        # 斜率是 (y2-y1)/(x2-x1)
        k = (y2-y1)/(x2-x1)
        # 节点是 y1 - 斜率 * x1
        b = y1 - k*x1
        # 放入第三个点，查看是否在直线上
        if y3 == k*x3+b:
            return False
        return True
