# 在一个sorted list中找到以x为中心，最近的k个元素（如果x在list中，它就是离它自己最近的元素）
# 要求：1.返回值是sorted，2.如果k还剩1，且此时有两个同等距离的元素，选较小者
# 解法一：使用heap来保存每个元素和x的距离，返回前k个
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = []
        for i in arr:
            l.append((abs(i-x), i))
        heapq.heapify(l)
        return sorted([x[1] for x in heapq.nsmallest(k, l)])


# 解法二：two pointer
# 首先从整个arr出发，对比两个元素与x的距离，然后一路缩减到只有k个元素为止
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l >= k:
            if x - arr[l] <= arr[r] - x:
                r -= 1
            else:
                l += 1
        return arr[l:r+1]


# 解法三：binary search 找到离x最近的元素（x可能就在list中），然后拓展

# 解法四：binary search，但是只找k个元素这个sublist的起止点（即left和right）
# https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2
			
            if x <= arr[mid]:
                right = mid
            elif x >= arr[mid + k]:
                left = mid + 1
            elif x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]


# 解法五：在四的基础上删减不必要的if statement
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2
			
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]