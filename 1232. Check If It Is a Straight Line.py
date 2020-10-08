class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 思路：用两个坐标建立方程（求出斜率再带回去求出weight），然后其他的坐标进行验证
        # 另一种思路：对于任意三点而言，两两斜率均相等（使用乘法来避免除以0）
        (x0, y0), (x1, y1) = coordinates[: 2] # [:2] 返回0和1,不包含2
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True

        
