# 解法1：
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 创建set
        city = set()
        # 添加元素
        for l in paths:
            city.add(l[1])
        # 删除元素：注意使用remove()时若元素不存在则会报错
        for l in paths:
            city.discard(l[0])
        # 获得set中唯一一个元素
        return next(iter(city))

# 解法2：python语法
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 1. * 会遍历paths中所有的元素并逐个输出
        # 2. zip()会将括号内所有元素，它们自己所拥有的元素，按顺序放在一起
        # 所以在这里，前两步结合就变成了：
        # 一个拥有两个元素的array，第一个元素是所有出发城市的tuple，第二个元素是所有抵达城市的tuple
        # 3. map是将第二个参数（一个数据结构）中所有的元素，作为参数放进第一个参数（一个方程）中
        # 所以最终得到的是2个set：A和B，A拥有所有的出发城市，B拥有所有的抵达城市
        A, B = map(set, zip(*paths))
        # B - A得到的是所有在B中但不在A中的元素，使用set.pop()获得该元素
        return (B - A).pop()
