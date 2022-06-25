# solution1: sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


# solution2: heapq module
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


# 06-12-2022
# 给一个list，找到第k大的元素
# 举例：[3,2,1,6,5,4], k = 2
# 因为sort后list = [1,2,3,4,5,6]，所以第2大的元素是5

# 暴力解：先sort再找

# 维持一个大小为k的heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [float('-inf')] * k
        heapq.heapify(h)
        for i in nums:
            heapq.heappushpop(h, i)
        ans = heapq.heappop(h)
        return ans