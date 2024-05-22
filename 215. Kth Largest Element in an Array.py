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


"""
Quickselect algorithm is used to find k-th smallest/largest element in unsorted array

Quicksort: O(nlogn) divide and conquer, pick pivot, get left part and right part, repeat
Quickselect: instead of recurring for both sides, only recur for one part

best: O(n), worst: O(n^2)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # turn question into: finding the len(nums)-k smallest element
        lo, hi = 0, len(nums) - 1

        # pick last element as pivot
        # rearrange array such that left side < pivot <= right side
        # return pivot new index
        def partition(a, lo, hi):
            pivot = a[hi]  
            i = lo
            for j in range(lo, hi):
                if a[j] < pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[hi] = a[hi], a[i]
            return i
        
        while lo < hi:
            j = partition(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break
        
        return nums[k]
        