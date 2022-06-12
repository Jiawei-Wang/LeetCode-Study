# 暴力解：将每个元素的下标以它的weight的数量加入一个list，从list中随机取一个返回
# space超标
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.weight = []
        for i in range(len(self.w)):
            self.weight += [i] * self.w[i]

    def pickIndex(self) -> int:
        index = random.randint(0, len(self.weight)-1)
        return self.weight[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# built in
class Solution:
    def __init__(self, w):
        self.w = w

    def pickIndex(self):
        return random.choices(range(len(self.w)), weights=self.w)[0]

    """
    choice() method returns a randomly selected element from the specified sequence，返回的是一个只有一个元素的list
    If a weights sequence is specified, selections are made according to the relative weights
    """


# built in
class Solution:
    def __init__(self, w):
        self.w = list(itertools.accumulate(w)) 
        # 将w中两两元素相加，然后返回一个值，然后再拿这个值和下一个元素相加，返回另一个值
        # 所以最后会得到[w[0], w[0]+w[1], w[0]+w[1]+w[2], etc]
        # 举例：
        # import itertools
        # a = [1,2,3,4]
        # for item in itertools.accumulate(a):
        # print(item)：1,3,6,10

        
    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
        # 从w最后一个元素的值（即w[0]+w[1]+w[2]+etc）中随机取一个数字，然后找到该数字在w中（如果要进行插入操作）应该存在的最左边的位置
        # 举例
        # w = [1,2,3,4]
        # 新的w = [1,3,6,10]
        # 随机取5, 则应当返回2