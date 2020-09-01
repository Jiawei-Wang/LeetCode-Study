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
