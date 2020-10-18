from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        bigger = deque() # bigger是一个递减queue
        for i, n in enumerate(nums):
            # 将queue尾部开始所有小于该元素的元素都pop出来
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # 将该元素加入queue尾部
            bigger += [i]

            # 如果尾部元素和头部元素在nums中距离超过k, 则pop掉头部元素
            if i - bigger[0] >= k:
                bigger.popleft()

            # 只有当遍历到第k个元素时, 才开始向res中添加元素
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res

    # 有空时还需要再过一遍这道题