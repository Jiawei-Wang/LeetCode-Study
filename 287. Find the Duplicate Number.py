class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
        return -1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Map = {}
        for i in nums:
            if i in Map:
                return i
            Map[i] = 1
        return -1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n-1

        while left <right:
            mid = left + (right -left) //2
            counter = 0
            for i in range(n):
                if nums[i] <= mid:
                    counter +=1
            if counter > mid:
                right = mid
            else:
                left = mid + 1
        return left


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
