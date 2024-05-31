class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        for i in range(len(nums)):
            if i == len(nums)-1:
                return i if left == 0 else -1

            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i+1]