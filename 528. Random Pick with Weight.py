# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# 暴力解：create multiple copies of elements based on weight
# space超标
class Solution:

    def __init__(self, w: List[int]):
        self.weight = []
        for i in range(len(w)):
            self.weight += [i] * w[i]
        # for example: w = [5, 10, 15]
        # we will have 5 0s, 10 1s and 15 2s in self.weight

    def pickIndex(self) -> int:
        index = random.randint(0, len(self.weight)-1)
        return self.weight[index]


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


# 将上面的built in换成正常代码
# accumulated freq sum + binary search
class Solution:
    def __init__(self, w: List[int]):
        self.weights = w
        self.length = len(w)
        for i in range(1,self.length):
            self.weights[i] += self.weights[i-1]
        self.sum = self.weights[-1]

    def pickIndex(self):
        seed = random.randint(1,self.sum)
        l,r = 0, self.length-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.weights[mid]:
                r = mid
            else:
                l = mid+1
        return l

    # why it works
    # w = [5, 10, 15]: we have 5 zeros, 10 ones and 15 twos
    # brute force solution is to actually create 30 seends for all 3 candidates in the memory
    # but instead we assign a range for each candidate, a seed is just a number in this range
    # so when a seed is picked, we binary search to find which candidate stays in this range
    # self.weights = [5, 15, 30], self.sum = 30
    # which means we have in total 30 seeds, 1 to 5 is zero, 6 to 15 is one, 16 to 30 is two
    # pick a seed between 1 and 30, if seed = 14, we return 1


# 还有一个更优化的答案：
# https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation