# Sorting Algorithms in python


# Built-in: sorted()
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


# Built-in: sort()
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


# Module: heapq
class Solution: 
    def sortArray(self, nums: List[int]) -> List[int]:
        answer = []
        heapq.heapify(nums)
        # nums is not sorted 
        # we need to pop from nums and append to answer
        # also we need to use heapq.heappop(nums) not nums.pop()
        # same reason: nums itself is not sorted
        while nums: 
            answer.append(heapq.heappop(nums))
        return answer


# Standard Library: bisect.insort()
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            bisect.insort(answer, num)
        return answer


# Insertion Sort: n^2
# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置后
# 6. 重复步骤2~5
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for unsorted_index in range(1, len(nums)):
            key = nums[unsorted_index]
            sorted_index = unsorted_index - 1
            while sorted_index >= 0 and key < nums[sorted_index]:
                nums[sorted_index + 1] = nums[sorted_index]
                sorted_index -= 1
            nums[sorted_index + 1] = key
        return nums


# Insertion Sort: recursion
class Solution:
    # keep popping from nums, till we find location for val
    # append val, then add all popped elements back
    def insert(self, nums, val):
        if not nums or val >= nums[-1]:
            nums.append(val)
            return
        last = nums.pop()
        self.insert(nums, val)
        nums.append(last)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        last = nums.pop()
        self.sortArray(nums)
        self.insert(nums, last)
        
        return nums


# Selection Sort: n^2
# find min/max element, put it into location, then find min/max element in rest of array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j            
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


# Bubble Sort: n^2
# 1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个。
# 2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 3. 针对所有的元素重复以上的步骤，除了最后一个。
# 4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # each loop we get the maximum and put it at the end
        for i in range(n):
            for j in range(n-i-1): 
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


# Quick Sort: nlogn
# divide and conquer
# 1. 挑选基准值：从数列中挑出一个元素，称为“基准”（pivot），
# 2. 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成，
# 3. 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivot = nums[len(nums)-1]
        less_than_pivot = [x for x in nums[:-1] if x <= pivot]
        greater_than_pivot = [x for x in nums[:-1] if x > pivot]

        return self.sortArray(less_than_pivot) + [pivot] + self.sortArray(greater_than_pivot)


# Merge Sort: divide and conquer, nlogn
class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        # merge two sorted lists together
        def merge(left, right):
            merged = []
            left_index, right_index = 0, 0
            # Compare elements from left and right halves and merge them
            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1
            # Append remaining elements from left or right halves
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])
            return merged
        
        
        if len(arr) <= 1:
            return arr

        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort each half
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        # Merge the sorted halves
        return merge(left_half, right_half)


# Counting Sort: n+k
class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        # for example: arr = [5, 1, 1, 2, 0, 0]
        if not arr:
            return arr

        # Find the maximum and minimum elements in the array
        max_val = max(arr)
        min_val = min(arr)

        # Initialize the count array
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements

        # Count the occurrences of each element
        for num in arr:
            count[num - min_val] += 1

        # count = [2, 2, 1, 0, 0, 1]
        # 2 elements are = min_val
        # 2 elements are = min_val + 1
        # ...
        # 1 element is = max_val

        # Modify the count array to store the cumulative count of each element
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # count = [2, 4, 5, 5, 5, 6]
        # min_val elements occupy index = 2
        # min_val + 1 elements occupy index = 4
        # ...
        # max_val element occupies index = 6

        # Output array to store the sorted order
        output = [0] * len(arr)

        # Build the output array by placing elements in their correct position
        for num in reversed(arr):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1

        return output


# TODO: Radix Sort, Bucket Sort