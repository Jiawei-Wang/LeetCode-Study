# 题目理解：从1到n一共n个正整数，将所有的数字以每个digit之和来划分，分为若干list
# 举例：n = 25
# 那么从1到25，所有数字中digit之和为6的为：[6, 15, 24]
# 其长度为3
# 题目要求返回最长长度的list的总个数
# 读题感想：
# 1. 题目已知n的范围从1到10000，所以digit之和最大为36（出现在9999）
# 2. 对于一个和，list的长度其实就是找到所有可能组合中符合条件的组合，举例：sum = 5，那么找出所有组合中 1.和为5，2.组成的数字<=n的组合


# simulation
# 将所有数字走一遍，记录所有list（不保留元素，只保留元素个数）
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 因为x最大为10000，所以此function为constant time
        def getSum(x):
            s = 0
            while x != 0:
                d = x % 10 
                s += d
                x //= 10
            return s
        
        # constant space
        digit = [0] * 36
        
        # O(n)
        for i in range(1, n+1):
            digit[getSum(i)-1] += 1
        
        return digit.count(max(digit))