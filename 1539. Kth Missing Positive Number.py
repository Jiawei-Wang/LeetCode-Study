# 解法1：步进
# Time: n
# Space: 1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 一个变量记录当前遍历到的数字
        current = 1
        # 一个变量记录当前找到几个missing number
        count = 0
        # 一个变量记录当前遍历到的arr的位置
        index = 0

        while count < k and index < len(arr):
            if current != arr[index]:
                count += 1
            else:
                index += 1
            current += 1

        return current + k - count - 1


# 解法2：找出arr中可以穿插进多少元素
# Time: n
# Space: 1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # start记录的是当前所在元素的值，初始为0
        start = 0

        # 遍历所有元素
        for i in range(len(arr)):

            # 如果这个元素和start之间能插入的元素个数小于当前所剩 k 的话，k 减去对应个数
            if k > (arr[i] - start - 1):
                k -= (arr[i] - start - 1)
            # 如果个数大于等于所剩 k 的话，答案就是 start + k
            else:
                return start + k

            # 每次更新start的值
            start = arr[i]

        # 如果遍历完也没找到答案的话，答案是最后一个元素的值 + k所剩的值
        return arr[-1]+k


# 解法3：反向遍历
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for index in range(len(arr)-1, -1, -1):
            if k + index + 1 > arr[index]:
                return k + index + 1
        return k


# 解法4: 二分查找
# Time: logn
# Space: 1
class Solution:
    def findKthPositive(self, A: List[int], k: int) -> int:
        l, r = 0, len(A)
        while l < r:
            m = (l + r) // 2
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k
