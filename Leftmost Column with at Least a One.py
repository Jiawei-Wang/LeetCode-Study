# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # 每个row都是非降序排列
        # 找出含有 '1' 的最早一个column
        # 不能直接访问 mat，同时也不可以对mat使用超过1000次get()

        # 先获得row和column的长度
        N, M = binaryMatrix.dimensions()

        # 对该row所有元素进行二分查找
        def find(row):
            left = 0
            right = M

            while left < right:
                middle = (left + right) // 2

                if binaryMatrix.get(row, middle) == 0:
                    left = middle + 1
                else:
                    right = middle
            return left

        # 需要返回的是最佳的column下标
        best = M
        # 找到每一row最优的column下标
        for row in range(N):
            column = find(row)
            best = min(best, column)

        if best == M:
            return -1
        return best
