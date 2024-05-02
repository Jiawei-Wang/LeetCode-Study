# solution1: sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


# solution2: heapq
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


# 维持一个大小为k的heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [float('-inf')] * k
        heapq.heapify(h)
        for num in nums:
            heapq.heappushpop(h, num)
        ans = heapq.heappop(h)
        return ans